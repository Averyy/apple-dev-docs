# CKDBZone

**Framework**: CKTool JS  
**Kind**: struct

An object that represents a CloudKit database zone.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
dictionary CKDBZone {
	string zoneName;
	string canonicalName;
	string zoneType;
	boolean isDefaultZone;
	boolean? isSharable;
	boolean? isEligibleForZoneShare;
	boolean? isEligibleForHierarchicalShare;
	string? ownerRecordName;
	string? changeToken;
	boolean atomic;
};
```

#### Overview

A zone is a logical separation of records within a single database. Features are often associated with an entire zone. For example, a zone may be optionally shared from one user to another.

In JavaScript, this is a plain object with properties as described.

In TypeScript, this type is imported in the following way:

```javascript
import type { CKDBZone } from "@apple/cktool.database";
```

## Topics

### Instance Properties
- [atomic](ckdbzone/atomic.md)
  A Boolean value that indicates whether a zone allows atomic changes of multiple records.
- [canonicalName](ckdbzone/canonicalname.md)
  The unique identifier for a zone within a database.
- [changeToken](ckdbzone/changetoken.md)
  The client change token for the zone.
- [isDefaultZone](ckdbzone/isdefaultzone.md)
  A Boolean value that indicates whether the zone is a default zone.
- [isEligibleForHierarchicalShare](ckdbzone/iseligibleforhierarchicalshare.md)
  A Boolean value that indicates whether zone is eligible for Hierarchical Share.
- [isEligibleForZoneShare](ckdbzone/iseligibleforzoneshare.md)
  A Boolean value that indicates whether zone is eligible for Zone Share.
- [isSharable](ckdbzone/issharable.md)
  A Boolean value that indicates whether records in this zone can be shared.
- [ownerRecordName](ckdbzone/ownerrecordname.md)
  The owner of the zone.
- [zoneName](ckdbzone/zonename.md)
  The name that identifies the record zone.
- [zoneType](ckdbzone/zonetype.md)
  The type for the zone.

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

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/ckdbzone)*