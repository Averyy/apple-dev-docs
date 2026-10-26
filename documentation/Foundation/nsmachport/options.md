# NSMachPort.Options

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

```c
enum NSMachPortOptions : NSUInteger;
```

## Topics

### Constants
- [static var deallocateReceiveRight: NSMachPort.Options](./options/deallocatereceiveright.md)
  Remove a receive right when the `NSMachPort` object is invalidated or destroyed.
- [static var deallocateSendRight: NSMachPort.Options](./options/deallocatesendright.md)
  Deallocate a send right when the `NSMachPort` object is invalidated or destroyed.
- [NSMachPortDeallocateNone](../nsmachportoptions/nsmachportdeallocatenone.md)
  Do not remove any send or receive rights.
### Initializers
- [init(rawValue: UInt)](./options/init%28rawvalue%29.md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmachport/options)*