# CKRecordZone.Capabilities

**Framework**: CloudKit  
**Kind**: struct  
**Role**: Structure

The capabilities that a record zone supports.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
struct Capabilities
```

```c
enum CKRecordZoneCapabilities : NSUInteger;
```

## Topics

### Creating Zone Capabilities
- [init(rawValue: UInt)](./capabilities-swift.struct/init%28rawvalue%29.md)
  Creates a set of capabilities for a record zone.
### Zone Capabilities
- [static var atomic: CKRecordZone.Capabilities](./capabilities-swift.struct/atomic.md)
  A capability that allows atomic changes of multiple records.
- [static var fetchChanges: CKRecordZone.Capabilities](./capabilities-swift.struct/fetchchanges.md)
  A capability for fetching only the changed records from a zone.
- [static var sharing: CKRecordZone.Capabilities](./capabilities-swift.struct/sharing.md)
  A capability for sharing a specific hierarchy of records.
- [static var zoneWideSharing: CKRecordZone.Capabilities](./capabilities-swift.struct/zonewidesharing.md)
  A capability for sharing the entire contents of a record zone.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Getting the Zone Attributes
- [var zoneID: CKRecordZone.ID](./zoneid.md)
  The unique ID of the zone.
- [var capabilities: CKRecordZone.Capabilities](./capabilities-swift.property.md)
  The capabilities that the zone supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecordzone/capabilities-swift.struct)*