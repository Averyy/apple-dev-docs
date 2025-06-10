# VASReadResult.ReadEntry.Status

**Framework**: ProximityReader  
**Kind**: enum

Status words that indicate the possible read outcomes.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.0+

## Declaration

```swift
enum Status
```

## Topics

### Getting the status
- [VASReadResult.ReadEntry.Status.success](vasreadresult/readentry/status-swift.enum/success.md)
- [VASReadResult.ReadEntry.Status.incorrectData](vasreadresult/readentry/status-swift.enum/incorrectdata.md)
- [VASReadResult.ReadEntry.Status.unsupportedApplicationVersion](vasreadresult/readentry/status-swift.enum/unsupportedapplicationversion.md)
- [VASReadResult.ReadEntry.Status.userInterventionRequired](vasreadresult/readentry/status-swift.enum/userinterventionrequired.md)
- [VASReadResult.ReadEntry.Status.vasDataNotActivated](vasreadresult/readentry/status-swift.enum/vasdatanotactivated.md)
- [VASReadResult.ReadEntry.Status.vasDataNotFound](vasreadresult/readentry/status-swift.enum/vasdatanotfound.md)
- [VASReadResult.ReadEntry.Status.wrongCommandLength](vasreadresult/readentry/status-swift.enum/wrongcommandlength.md)
- [VASReadResult.ReadEntry.Status.wrongP1P2](vasreadresult/readentry/status-swift.enum/wrongp1p2.md)
### Initializers
- [init?(rawValue: Int)](vasreadresult/readentry/status-swift.enum/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Instance Properties
- [var rawValue: Int](vasreadresult/readentry/status-swift.enum/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [VASReadResult.ReadEntry.Status.RawValue](vasreadresult/readentry/status-swift.enum/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [Equatable Implementations](vasreadresult/readentry/status-swift.enum/equatable-implementations.md)
- [RawRepresentable Implementations](vasreadresult/readentry/status-swift.enum/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let status: VASReadResult.ReadEntry.Status](vasreadresult/readentry/status-swift.property.md)
  The status word that represents the outcome of the VAS read attempt for this reward pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/vasreadresult/readentry/status-swift.enum)*