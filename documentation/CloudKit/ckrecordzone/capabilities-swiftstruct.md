# CKRecordZone.Capabilities

**Framework**: CloudKit  
**Kind**: struct

The capabilities that a record zone supports.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
struct Capabilities
```

## Topics

### Creating Zone Capabilities
- [init(rawValue: UInt)](ckrecordzone/capabilities-swift.struct/init(rawvalue:).md)
  Creates a set of capabilities for a record zone.
### Zone Capabilities
- [static var atomic: CKRecordZone.Capabilities](ckrecordzone/capabilities-swift.struct/atomic.md)
  A capability that allows atomic changes of multiple records.
- [static var fetchChanges: CKRecordZone.Capabilities](ckrecordzone/capabilities-swift.struct/fetchchanges.md)
  A capability for fetching only the changed records from a zone.
- [static var sharing: CKRecordZone.Capabilities](ckrecordzone/capabilities-swift.struct/sharing.md)
  A capability for sharing a specific hierarchy of records.
- [static var zoneWideSharing: CKRecordZone.Capabilities](ckrecordzone/capabilities-swift.struct/zonewidesharing.md)
  A capability for sharing the entire contents of a record zone.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var zoneID: CKRecordZone.ID](ckrecordzone/zoneid.md)
  The unique ID of the zone.
- [var capabilities: CKRecordZone.Capabilities](ckrecordzone/capabilities-swift.property.md)
  The capabilities that the zone supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecordzone/capabilities-swift.struct)*