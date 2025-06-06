# CKDBUserNameComponents

**Framework**: CKTool JS  
**Kind**: struct

An object that represents the user’s name.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
dictionary CKDBUserNameComponents {
	string? givenName;
	string? middleName;
	string? familyName;
	string? namePrefix;
	string? nameSuffix;
	string? nickname;
	string? phoneticRepresentation;
};
```

#### Overview

In JavaScript, this is a plain object with properties as described.

In TypeScript, this type is imported in the following way:

```javascript
import type { CKDBUserNameComponents } from "@apple/cktool.database";
```

## Topics

### Instance Properties
- [familyName](ckdbusernamecomponents/familyname.md)
  The user’s last name.
- [givenName](ckdbusernamecomponents/givenname.md)
  The user’s first name.
- [middleName](ckdbusernamecomponents/middlename.md)
  The user’s middle name.
- [namePrefix](ckdbusernamecomponents/nameprefix.md)
  The user’s prefix.
- [nameSuffix](ckdbusernamecomponents/namesuffix.md)
  The user’s suffix.
- [nickname](ckdbusernamecomponents/nickname.md)
  The user’s nickname.
- [phoneticRepresentation](ckdbusernamecomponents/phoneticrepresentation.md)
  A phonetic representation of the user’s name.

## See Also

- [CKDBAsset](ckdbasset.md)
  An object that represents an asset uploaded to CloudKit.
- [CKDBAssetUploadUrlResponse](ckdbassetuploadurlresponse.md)
  An object that represents the results of creating an asset upload URL.
- [CKDBChangeMetadata](ckdbchangemetadata.md)
  An object that represents metadata about a record change via creation or modification.
- [CKDBCreateAssetUploadUrlRequestBody](ckdbcreateassetuploadurlrequestbody.md)
  An object that represents the request for creating an asset upload URL.
- [CKDBCreateRecordRequestBody](ckdbcreaterecordrequestbody.md)
  An object that represents the request to create a new record.
- [CKDBCreateZoneRequestBody](ckdbcreatezonerequestbody.md)
  An object that represents the request to create a new zone.
- [CKDBDeleteRecordsByQueryRequestBody](ckdbdeleterecordsbyqueryrequestbody.md)
  An object that represents the request to delete multiple records that match a query.
- [CKDBDeletedRecordResult](ckdbdeletedrecordresult.md)
  An object that represents a deleted record result.
- [CKDBErrorRecordResult](ckdberrorrecordresult.md)
  An object that represents a record lookup failure.
- [CKDBExistingRecordResult](ckdbexistingrecordresult.md)
  An object that represents a successful record result.
- [CKDBForRecord](ckdbforrecord.md)
  An object that represents a record that is being shared.
- [CKDBLocation](ckdblocation.md)
  An object that represents a location field value.
- [CKDBLookupRecordsRequestBody](ckdblookuprecordsrequestbody.md)
  An object that represents the request for looking up multiple records by record name.
- [CKDBLookupRecordsResponse](ckdblookuprecordsresponse.md)
  An object that represents the results of a batch record lookup operation.
- [CKDBModifyRecordRequestBody](ckdbmodifyrecordrequestbody.md)
  An object that represents the request for updating an existing record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/ckdbusernamecomponents)*