# CKSyncEngineFailedZoneSave

**Framework**: CloudKit  
**Kind**: class  
**Role**: Class

An object that describes an unsuccessful attempt to modify a single record zone.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```objc
@interface CKSyncEngineFailedZoneSave : NSObject
```

## Topics

### Accessing the record zone
- [recordZone](./cksyncenginefailedzonesave/recordzone.md)
  The record zone that CloudKit is unable to modify.
### Accessing the error
- [error](./cksyncenginefailedzonesave/error.md)
  An error that describes the reason for the unsuccessful attempt to modify the associated record zone.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Accessing failed changes
- [failedZoneDeletes](./cksyncenginesentdatabasechangesevent/failedzonedeletes.md)
  The unique identifiers of the record zones CloudKit is unable to delete, and the reasons why.
- [failedZoneSaves](./cksyncenginesentdatabasechangesevent/failedzonesaves.md)
  The record zones that CloudKit is unable to modify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginefailedzonesave)*