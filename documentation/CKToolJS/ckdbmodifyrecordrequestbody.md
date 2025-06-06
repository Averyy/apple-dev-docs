# CKDBModifyRecordRequestBody

**Framework**: CKTool JS  
**Kind**: struct

An object that represents the request for updating an existing record.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
dictionary CKDBModifyRecordRequestBody {
	string recordType;
	string? recordChangeTag;
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
import type { CKDBModifyRecordRequestBody } from "@apple/cktool.database";
```

## Topics

### Instance Properties
- [createShortGuid](ckdbmodifyrecordrequestbody/createshortguid.md)
  A Boolean value that indicates whether to create a short GUID for sharing this record.
- [fields](ckdbmodifyrecordrequestbody/fields.md)
  The dictionary of key-value pairs whose keys are the record field names and values are field-value dictionaries.
- [forRecord](ckdbmodifyrecordrequestbody/forrecord.md)
- [parent](ckdbmodifyrecordrequestbody/parent.md)
- [participants](ckdbmodifyrecordrequestbody/participants.md)
  The array of participants in the shared record.
- [publicPermission](ckdbmodifyrecordrequestbody/publicpermission.md)
- [recordChangeTag](ckdbmodifyrecordrequestbody/recordchangetag.md)
  A string containing the server change token for the record.
- [recordType](ckdbmodifyrecordrequestbody/recordtype.md)
  The name of the record type.
- [share](ckdbmodifyrecordrequestbody/share.md)

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
- [CKDBNullableReference](ckdbnullablereference.md)
  An object that represents a reference to another record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/ckdbmodifyrecordrequestbody)*