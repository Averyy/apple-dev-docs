# CKDBLocation

**Framework**: CKTool JS  
**Kind**: struct

An object that represents a location field value.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
dictionary CKDBLocation {
	Double latitude;
	Double longitude;
	Double? altitude;
	Double? horizontalAccuracy;
	Double? verticalAccuracy;
	Double? course;
	Double? speed;
	date? timestamp;
};
```

#### Overview

In JavaScript, this is a plain object with properties as described.

In TypeScript, this type is imported in the following way:

```javascript
import type { CKDBLocation } from "@apple/cktool.database";
```

## Topics

### Instance Properties
- [altitude](ckdblocation/altitude.md)
  The altitude measured in meters.
- [course](ckdblocation/course.md)
  The direction in which the device is traveling.
- [horizontalAccuracy](ckdblocation/horizontalaccuracy.md)
  The radius of uncertainty for the location measured in meters.
- [latitude](ckdblocation/latitude.md)
  The latitude of the coordinate point.
- [longitude](ckdblocation/longitude.md)
  The longitude of the coordinate point.
- [speed](ckdblocation/speed.md)
  The instantaneous speed of the device in meters per second.
- [timestamp](ckdblocation/timestamp.md)
  The time at which this location was determined.
- [verticalAccuracy](ckdblocation/verticalaccuracy.md)
  The validity of the altitude values and their estimated uncertainty measured in meters.

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
- [CKDBLookupRecordsRequestBody](ckdblookuprecordsrequestbody.md)
  An object that represents the request for looking up multiple records by record name.
- [CKDBLookupRecordsResponse](ckdblookuprecordsresponse.md)
  An object that represents the results of a batch record lookup operation.
- [CKDBModifyRecordRequestBody](ckdbmodifyrecordrequestbody.md)
  An object that represents the request for updating an existing record.
- [CKDBNullableReference](ckdbnullablereference.md)
  An object that represents a reference to another record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/ckdblocation)*