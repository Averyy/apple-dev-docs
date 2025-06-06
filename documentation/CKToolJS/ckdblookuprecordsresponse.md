# CKDBLookupRecordsResponse

**Framework**: CKTool JS  
**Kind**: struct

An object that represents the results of a batch record lookup operation.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
dictionary CKDBLookupRecordsResponse {
	CKDBRecordResult[] recordResults;
};
```

#### Overview

In JavaScript, this is a plain object with properties as described.

In TypeScript, this type is imported in the following way:

```javascript
import type { CKDBLookupRecordsResponse } from "@apple/cktool.database";
```

## Topics

### Instance Properties
- [recordResults](ckdblookuprecordsresponse/recordresults.md)
  The array of `CKDBRecordResult` objects that represent a record.

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
- [CKDBModifyRecordRequestBody](ckdbmodifyrecordrequestbody.md)
  An object that represents the request for updating an existing record.
- [CKDBNullableReference](ckdbnullablereference.md)
  An object that represents a reference to another record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/ckdblookuprecordsresponse)*