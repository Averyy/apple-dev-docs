# CloudKit

**Framework**: CloudKit  
**Kind**: module

Store structured app and user data in iCloud containers that all users of your app can share.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

#### Overview

The CloudKit framework provides interfaces for moving data between your app and your iCloud containers. You use CloudKit to store your app’s existing data in the cloud so that the user can access it on multiple devices. You can also store data in a public area where all users can access it.

##### Using the Cloudkit Framework

CloudKit isn’t a replacement for your app’s existing data objects. Instead, CloudKit provides complementary services for managing the transfer of data to and from iCloud servers. Because it provides minimal offline caching support, CloudKit relies on the presence of the network and, optionally, a valid iCloud account. A valid iCloud account is only necessary when you want to save data that is specific to a single user. Apps can always store data in a public area that is readable by all users.

Records are at the heart of all data transactions in CloudKit. A record is a dictionary of key-value pairs that represents the data you want to save. You can add new keys and values to records at any time, and you can create links between related records to organize your data. The [`CKRecord`](ckrecord.md) class defines the interfaces for managing the contents of records. CloudKit also relies heavily on the use of [`Operation`](https://developer.apple.com/documentation/Foundation/Operation) objects to manage the asynchronous transfer of data to and from the server.

Before using CloudKit, make sure it’s the most suitable option for your app. For more information, see [`Deciding whether CloudKit is right for your app`](deciding-whether-cloudkit-is-right-for-your-app.md).

> **Note**:  The classes of the CloudKit framework aren’t for subclassing. Use these classes as-is to save, retrieve, and manipulate data in iCloud. In addition, many of the protocols of this framework aren’t for adoption by classes outside of CloudKit and UIKit. Each protocol reference document includes information about whether you can adopt the protocol in your own classes.

 The classes of the CloudKit framework aren’t for subclassing. Use these classes as-is to save, retrieve, and manipulate data in iCloud. In addition, many of the protocols of this framework aren’t for adoption by classes outside of CloudKit and UIKit. Each protocol reference document includes information about whether you can adopt the protocol in your own classes.

## Topics

### Essentials
- [Deciding whether CloudKit is right for your app](deciding-whether-cloudkit-is-right-for-your-app.md)
  Explore the various options you have for using iCloud to store and sync your app’s data.
- [Enabling CloudKit in Your App](enabling-cloudkit-in-your-app.md)
  Configure your app to store data in iCloud using CloudKit.
### Schemas
- [Designing and Creating a CloudKit Database](designing-and-creating-a-cloudkit-database.md)
  Create a schema to store your app’s objects as records in iCloud using CloudKit.
- [Managing iCloud Containers with CloudKit Database App](managing-icloud-containers-with-cloudkit-database-app.md)
  Inspect and modify the schema and data for your app’s iCloud container.
- [class CKRecordZone](ckrecordzone.md)
  A database partition that contains related records.
- [class CKRecord](ckrecord.md)
  A collection of key-value pairs that store your app’s data.
- [CKRecord.Reference](ckrecord/reference.md)
  A relationship between two records in a record zone.
- [class CKAsset](ckasset.md)
  An external file that belongs to a record.
- [Integrating a Text-Based Schema into Your Workflow](integrating-a-text-based-schema-into-your-workflow.md)
  Define and update your schema with the CloudKit Schema Language.
### Records
- [Local Records](local-records.md)
  Manipulate records on-device and save changes to the server.
- [Remote Records](remote-records.md)
  Use subscriptions and change tokens to efficiently manage modifications to remote records.
- [class CKSyncEngine](cksyncengine-5sie5.md)
  An object that manages the synchronization of local and remote record data.
- [Shared Records](shared-records.md)
  Share one or more records with other iCloud users.
### User discovery
- [class CKUserIdentity](ckuseridentity.md)
  The identity of a user.
- [CKUserIdentity.LookupInfo](ckuseridentity/lookupinfo-swift.class.md)
  The criteria to use when searching for discoverable iCloud users.
### Core objects
- [class CKContainer](ckcontainer.md)
  A conduit to your app’s databases.
- [class CKDatabase](ckdatabase.md)
  An object that represents a collection of record zones and subscriptions.
- [class CKOperationGroup](ckoperationgroup.md)
  An explicit association between two or more operations.
### Privacy
- [Encrypting User Data](encrypting-user-data.md)
  Deploy industry-standard security technologies using CloudKit encryption.
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
### Errors
- [let CKErrorDomain: String](ckerrordomain.md)
  The error domain for CloudKit errors.
- [struct CKError](ckerror.md)
  A type that describes a CloudKit error.
- [CKError.Code](ckerror/code.md)
  The error codes that CloudKit returns.
- [let CKErrorRetryAfterKey: String](ckerrorretryafterkey.md)
  The key to retrieve the number of seconds to wait before you retry a request.
- [let CKErrorUserDidResetEncryptedDataKey: String](ckerroruserdidresetencrypteddatakey.md)
  The key that determines whether CloudKit deletes a record zone because of a user action.
- [let CKPartialErrorsByItemIDKey: String](ckpartialerrorsbyitemidkey.md)
  The key to retrieve partial errors.
- [Record Changed Error Keys](record-changed-error-keys.md)
  Constants that represent conflicting records in a save operation.
### Deprecated
- [Deprecated Symbols](deprecated-symbols.md)
  Review unsupported symbols and their replacements.
### Variables
- [let CKRecordParentKey: String](ckrecordparentkey-1elhg.md)
- [let CKRecordShareKey: String](ckrecordsharekey-gc8w.md)
- [let CKRecordTypeShare: String](ckrecordtypeshare-7lec1.md)
- [let CKRecordTypeUserRecord: String](ckrecordtypeuserrecord-6iwgn.md)
- [let CKRecordZoneDefaultName: String](ckrecordzonedefaultname-1uuiu.md)
- [let CKShareThumbnailImageDataKey: String](cksharethumbnailimagedatakey-rxjd.md)
- [let CKShareTitleKey: String](cksharetitlekey-1cs9j.md)
- [let CKShareTypeKey: String](cksharetypekey-5m83p.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/CloudKit)*