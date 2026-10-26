# NSMachPortDeallocateNone

**Framework**: Foundation  
**Kind**: case  
**Role**: Enumeration Case

Do not remove any send or receive rights.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
NSMachPortDeallocateNone
```

## See Also

### Constants
- [static var deallocateReceiveRight: NSMachPort.Options](../nsmachport/options/deallocatereceiveright.md)
  Remove a receive right when the `NSMachPort` object is invalidated or destroyed.
- [static var deallocateSendRight: NSMachPort.Options](../nsmachport/options/deallocatesendright.md)
  Deallocate a send right when the `NSMachPort` object is invalidated or destroyed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmachportoptions/nsmachportdeallocatenone)*