# CKDBErrorRecordResult

**Framework**: CKTool JS  
**Kind**: struct

An object that represents a record lookup failure.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
dictionary CKDBErrorRecordResult {
	string type;
	string? recordName;
	string errorCode;
	string message;
};
```

#### Overview

The server returns a CKDBErrorRecordResult object when looking up a record fails as part of a batch record lookup operation.

In JavaScript, this is a plain object with properties as described.

In TypeScript, this type is imported in the following way:

```javascript
import type { CKDBErrorRecordResult } from "@apple/cktool.database";
```

## Topics

### Instance Properties
- [errorCode](ckdberrorrecordresult/errorcode.md)
  A string containing the code for the error that occurred.
- [message](ckdberrorrecordresult/message.md)
  A string that indicates the reason for the error.
- [recordName](ckdberrorrecordresult/recordname.md)
  The name of the record.
- [type](ckdberrorrecordresult/type.md)
  The type of the record result.

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

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/ckdberrorrecordresult)*