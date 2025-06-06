# CKDBRecord

**Framework**: CKTool JS  
**Kind**: struct

An object that represents a record in a database.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
dictionary CKDBRecord {
	string recordName;
	string recordType;
	string recordChangeTag;
	CKDBChangeMetadata created;
	CKDBChangeMetadata modified;
	dictionary fields;
	dictionary? otherSystemFields;
	CKDBNullableReference? share;
	CKDBNullableReference? parent;
	string? shortGuid;
	CKDBPermissionType? publicPermission;
	CKDBShareParticipant[]? participants;
	CKDBShareParticipant? owner;
	CKDBShareParticipant? currentUserParticipant;
	CKDBStableUrl? stableUrl;
	CKDBZoneId? zone;
};
```

#### Overview

In JavaScript, this is a plain object with properties as described.

In TypeScript, this type is imported in the following way:

```javascript
import type { CKDBRecord } from "@apple/cktool.database";
```

## Topics

### Instance Properties
- [created](ckdbrecord/created.md)
- [currentUserParticipant](ckdbrecord/currentuserparticipant.md)
- [fields](ckdbrecord/fields.md)
  The dictionary of key-value pairs whose keys are the record field names and values are field-value dictionaries.
- [modified](ckdbrecord/modified.md)
- [otherSystemFields](ckdbrecord/othersystemfields.md)
- [owner](ckdbrecord/owner.md)
- [parent](ckdbrecord/parent.md)
- [participants](ckdbrecord/participants.md)
  The array of participants in the shared record.
- [publicPermission](ckdbrecord/publicpermission.md)
- [recordChangeTag](ckdbrecord/recordchangetag.md)
  A string that contains the server change token for the record.
- [recordName](ckdbrecord/recordname.md)
  The unique name used to identify the record within a zone.
- [recordType](ckdbrecord/recordtype.md)
  The name of the record type.
- [share](ckdbrecord/share.md)
- [shortGuid](ckdbrecord/shortguid.md)
  A global unique identifier for this record used for sharing.
- [stableUrl](ckdbrecord/stableurl.md)
- [zone](ckdbrecord/zone.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/ckdbrecord)*