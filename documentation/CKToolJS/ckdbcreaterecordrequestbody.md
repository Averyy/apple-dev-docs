# CKDBCreateRecordRequestBody

**Framework**: CKTool JS  
**Kind**: struct

An object that represents the request to create a new record.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
dictionary CKDBCreateRecordRequestBody {
	string? recordName;
	string recordType;
	dictionary fields;
	boolean? createShortGuid;
	CKDBNullableReference? share;
	CKDBNullableReference? parent;
	CKDBForRecord? forRecord;
	CKDBPermissionType? publicPermission;
	CKDBShareParticipant[]? participants;
};
```

#### Overview

In JavaScript, this is a plain object with properties as described.

In TypeScript, this type is imported in the following way:

```javascript
import type { CKDBCreateRecordRequestBody } from "@apple/cktool.database";
```

## Topics

### Instance Properties
- [createShortGuid](ckdbcreaterecordrequestbody/createshortguid.md)
  A Boolean value that indicates whether to create a short GUID for sharing this record.
- [fields](ckdbcreaterecordrequestbody/fields.md)
  The dictionary of key-value pairs whose keys are the record field names and values are field-value dictionaries.
- [forRecord](ckdbcreaterecordrequestbody/forrecord.md)
- [parent](ckdbcreaterecordrequestbody/parent.md)
- [participants](ckdbcreaterecordrequestbody/participants.md)
  The array of participants in the shared record.
- [publicPermission](ckdbcreaterecordrequestbody/publicpermission.md)
- [recordName](ckdbcreaterecordrequestbody/recordname.md)
  The unique name used to identify the record within a zone.
- [recordType](ckdbcreaterecordrequestbody/recordtype.md)
- [share](ckdbcreaterecordrequestbody/share.md)

## See Also

- [CKDBAsset](ckdbasset.md)
  An object that represents an asset uploaded to CloudKit.
- [CKDBAssetUploadUrlResponse](ckdbassetuploadurlresponse.md)
  An object that represents the results of creating an asset upload URL.
- [CKDBChangeMetadata](ckdbchangemetadata.md)
  An object that represents metadata about a record change via creation or modification.
- [CKDBCreateAssetUploadUrlRequestBody](ckdbcreateassetuploadurlrequestbody.md)
  An object that represents the request for creating an asset upload URL.
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
- [CKDBNullableReference](ckdbnullablereference.md)
  An object that represents a reference to another record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/ckdbcreaterecordrequestbody)*