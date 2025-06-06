# CKDBStreamingAsset

**Framework**: CKTool JS  
**Kind**: struct

A streaming asset object that represents a streaming asset in CloudKit.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
dictionary CKDBStreamingAsset {
	string? fileSignature;
	string? referenceSignature;
	string? uploadReceipt;
	string? downloadUrl;
	Int64? requestedSize;
	Int64? uploadedSize;
	Int64? reservedSize;
};
```

#### Overview

CKDBStreamingAsset is used to start asset upload with minimal data.

In JavaScript, this is a plain object with properties as described.

In TypeScript, this type is imported in the following way:

```javascript
import type { CKDBStreamingAsset } from "@apple/cktool.database";
```

## Topics

### Instance Properties
- [downloadUrl](ckdbstreamingasset/downloadurl.md)
  The URL for accessing the asset.
- [fileSignature](ckdbstreamingasset/filesignature.md)
  The signature of a file returned from the file upload step.
- [referenceSignature](ckdbstreamingasset/referencesignature.md)
  The signature of a file returned from the asset upload step.
- [requestedSize](ckdbstreamingasset/requestedsize.md)
  The requested size of streaming asset.
- [reservedSize](ckdbstreamingasset/reservedsize.md)
  The reserved size of streaming asset.
- [uploadReceipt](ckdbstreamingasset/uploadreceipt.md)
  The receipt for uploading the asset.
- [uploadedSize](ckdbstreamingasset/uploadedsize.md)
  The uploaded size of streaming asset.

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

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/ckdbstreamingasset)*