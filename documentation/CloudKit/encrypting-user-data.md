# Encrypting User Data

**Framework**: Cloudkit

Deploy industry-standard security technologies using CloudKit encryption.

#### Overview

The CloudKit framework enforces strict policies and adopts privacy-preserving technologies to help you encrypt your users’ data. CloudKit stores data and protects data through account authentication using secure tokens. iCloud servers use encryption to ensure that only authorized users can access their data.

Encryption adds another layer of protection on top of account-based access control, and is available for data that’s sensitive or private to the user. CloudKit’s encrypted fields allow you to optionally add that second layer of cryptographic protection by choosing which fields the system encrypts within a [`CKRecord`](ckrecord.md).

Use encrypted fields to offer data encryption to your users in your CloudKit-based apps, such as Photos, Notes, Health, Home, and so forth. See the [`iCloud security overview`](https://developer.apple.comhttps://support.apple.com/en-us/HT202303) for more information.

##### Review Supported Database Types

CloudKit offers multiple database types, but not all databases support encryption.

##### Protect Users

CloudKit encrypts data with the key material in the user’s iCloud Keychain. If the user loses access to iCloud Keychain, CloudKit can’t access the key material that it previously used to encrypt the data, so iCloud can’t decrypt it.

Apple provides functionality to help users avoid this situation. However, there’s always a risk that a user might lose access to their iCloud keychain, and subsequently, can choose to start over by resetting to a new keychain. This may lead to a [`CKError.Code.zoneNotFound`](ckerror/code/zonenotfound.md) error from CloudKit that your app needs to handle. See the “Handle a User Keychain Reset” section below for more information.

##### Encrypt Fields in Cloudkit

Use the [`encryptedValues`](ckrecord/encryptedvalues.md) property to set a field on a `CKRecord` that instructs CloudKit to automatically encrypt data while writing, and decrypt it while reading. This method of encryption and decryption applies to most of the `Record` value types, including [`NSString`](https://developer.apple.com/documentation/Foundation/NSString), [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber), [`NSDate`](https://developer.apple.com/documentation/Foundation/NSDate), [`NSData`](https://developer.apple.com/documentation/Foundation/NSData), [`CLLocation`](https://developer.apple.com/documentation/CoreLocation/CLLocation), and [`NSArray`](https://developer.apple.com/documentation/Foundation/NSArray). However, there’s no encryption support for [`CKRecord.Reference`](ckrecord/reference.md) objects because they need to be visible to the server. CloudKit encrypts [`CKAsset`](ckasset.md) by default so you can’t set it as a value for the [`encryptedValues`](ckrecord/encryptedvalues.md) property.

Below is an example of the encrypted values property setting and getting [`NSData`](https://developer.apple.com/documentation/Foundation/NSData):

```swift
// Create a record.
let record = CKRecord(recordType: "MyRecordType")
        
// Define the encrypted field keys.
let dataKey = "dataKey"
let listKey = "listKey"
        
// Encrypt and decrypt arbitrary bytes of data.
record.encryptedValues[dataKey] = NSData()
let _ = record.encryptedValues[dataKey] as? NSData
        
// Encrypt a list of data bytes.
record.encryptedValues[listKey] = [
    NSData(),
    NSData()
]
        
// Retrieve the keys of all encrypted fields.
print(record.encryptedValues.allKeys())
```

Your CloudKit database schema needs to reflect which fields on specific record types require encryption. Update your schema in one of the following ways:

- Write a new field to a new or existing [`CKRecord`](ckrecord.md) through the [`encryptedValues`](ckrecord/encryptedvalues.md) property in the development environment of your container. This triggers a schema update to your development environment, which reflects in [`CloudKit console`](https://developer.apple.comhttps://icloud.developer.apple.com/dashboard/#home).
- Using CloudKit console, add a new field to a new record type in your development environment schema. Set the field type to the desired encrypted data type, such as Encrypted Double or Encrypted String.

![A screenshot of the CloudKit database app. The New Records menu item is in a selected state in the Schema section on the left, and the New Record Type pane displays on the right.](https://docs-assets.developer.apple.com/published/bb9ea638f2519ae15e7609b9f48417fd/media-3814031%402x.png)

Promote this schema change to your production environment before deploying any app changes to the App Store that rely on the new schema.

> **Note**:  The encrypted fields can’t have indexes because the server can’t read the fields. The encrypted fields also have to be newly introduced to an existing record or a new record. You can’t convert existing unencrypted fields in the CloudKit schema.

##### Use Assets

When creating or updating a [`CKRecord`](ckrecord.md) that contains a [`CKAsset`](ckasset.md), CloudKit breaks up the asset’s contents into chunks, and encrypts each chunk before storing it in the third-party services. CloudKit then encrypts the key for each chunk, which Apple maintains, with an asset key and stores the asset key on the relevant record.

CloudKit automatically stores the asset key in an encrypted field on the record in the private database, and by proxy, in the shared database. This means that CloudKit ultimately encrypts the asset data to a key in the user’s iCloud Keychain.

CloudKit doesn’t store the asset key in an encrypted field on the record in the public database because the record is accessible to anyone with access to that database.

For more information about security, see [`CloudKit security`](https://developer.apple.comhttps://support.apple.com/en-jo/guide/security/sec3d52c0374/1/web/1).

##### Handle a User Keychain Reset

When CloudKit is unable to decrypt the encrypted data, it returns a [`CKError.Code.zoneNotFound`](ckerror/code/zonenotfound.md) with an entry of [`CKErrorUserDidResetEncryptedDataKey`](ckerroruserdidresetencrypteddatakey.md) in its `userInfo` dictionary. This error can occur in any [`CKOperation`](ckoperation.md) that involves reading existing zones or records, such as:

- [`CKFetchRecordsOperation`](ckfetchrecordsoperation.md)
- [`CKFetchRecordZonesOperation`](ckfetchrecordzonesoperation.md)
- [`CKFetchRecordZoneChangesOperation`](ckfetchrecordzonechangesoperation.md)
- [`CKModifyRecordZonesOperation`](ckmodifyrecordzonesoperation.md)
- [`CKModifyRecordsOperation`](ckmodifyrecordsoperation.md)

When this error occurs, the data becomes permanently lost. Your app needs to handle this situation in the following manner:

- Delete the relevant zones.
- Recreate the relevant zones.
- Upload the locally cached data from the device to those zones. CloudKit encrypts the new data using new key material from the user’s iCloud Keychain.

> **Note**:  Users can also choose to manually delete their zones, resulting in data loss that isn’t related to resetting the keychain. In this case, any [`CKOperation`](ckoperation.md) that involves reading zones or records might encounter a [`CKError.Code.userDeletedZone`](ckerror/code/userdeletedzone.md) error. For this error, prompt for the user’s confirmation to purge the associated local records or zones.

##### Use Cloudkit Web Services

When making requests through the CloudKit web services interface with an authenticated user against compatible databases, you can:

- Save data in an encrypted field
- Pass an `isEncrypted` flag along with the payload in a [`CKModifyRecordsOperation`](ckmodifyrecordsoperation.md) records request

The web services handle the encryption and decryption for you. The rules regarding CloudKit database schema promotion remain the same for web services as they are for native CloudKit.

The following shows an example request for creating records with the encrypted fields:

```json
{
  "operations" : [ {
    "operationType" : "create",
    "record" : {
      "recordType" : "myRecordType",
      "fields" : {
        "myDoubleField" : {
          "value" : 0.55,
          "type" : "DOUBLE",
          "isEncrypted" : true
        },
        "myIntListField" : {
          "value" : [ 123, 456, 789 ],
          "type" : "INT64_LIST",
          "isEncrypted" : true
        }
      "recordName" : "recordWithEncryptedFields",
    }
  } ],
  "zoneID" : {
    "zoneName" : "myZone"
  }
}
```

## See Also

- [Providing User Access to CloudKit Data](providing-user-access-to-cloudkit-data.md)
  Provide users access to the data your app stores on their behalf.
- [Changing Access Controls on User Data](changing-access-controls-on-user-data.md)
  Restrict access to or remove restrictions from a user’s data at their request.
- [class CKFetchWebAuthTokenOperation](ckfetchwebauthtokenoperation.md)
  An operation that creates an authentication token for use with CloudKit web services.
- [Responding to Requests to Delete Data](responding-to-requests-to-delete-data.md)
  Provide options for users to delete their CloudKit data from your app.
- [Identifying an App’s Containers](identifying-an-app-s-containers.md)
  Use Xcode’s Project navigator to find the identifiers of active CloudKit containers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/CloudKit/encrypting-user-data)*