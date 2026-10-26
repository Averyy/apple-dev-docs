# deallocateReceiveRight

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Remove a receive right when the `NSMachPort` object is invalidated or destroyed.

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
static var deallocateReceiveRight: NSMachPort.Options { get }
```

```c
NSMachPortDeallocateReceiveRight
```

## See Also

### Constants
- [static var deallocateSendRight: NSMachPort.Options](./deallocatesendright.md)
  Deallocate a send right when the `NSMachPort` object is invalidated or destroyed.
- [NSMachPortDeallocateNone](../../nsmachportoptions/nsmachportdeallocatenone.md)
  Do not remove any send or receive rights.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmachport/options/deallocatereceiveright)*