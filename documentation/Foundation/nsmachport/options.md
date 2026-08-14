# NSMachPort.Options

**Framework**: Foundation  
**Kind**: struct

Used to remove access rights to a mach port when the `NSMachPort` object is invalidated or destroyed.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct Options
```

## Topics

### Constants
- [static var deallocateReceiveRight: NSMachPort.Options](nsmachport/options/deallocatereceiveright.md)
  Remove a receive right when the `NSMachPort` object is invalidated or destroyed.
- [static var deallocateSendRight: NSMachPort.Options](nsmachport/options/deallocatesendright.md)
  Deallocate a send right when the `NSMachPort` object is invalidated or destroyed.
### Initializers
- [init(rawValue: UInt)](nsmachport/options/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmachport/options)*