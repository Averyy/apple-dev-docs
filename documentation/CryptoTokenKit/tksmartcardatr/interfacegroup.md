# TKSmartCardATR.InterfaceGroup

**Framework**: CryptoTokenKit  
**Kind**: class  
**Role**: Class

A single interface-bytes group for a Smart Card ATR (Answer to Reset).

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class InterfaceGroup
```

```objc
@interface TKSmartCardATRInterfaceGroup : NSObject
```

#### Overview

You access instances of this class by calling the [`interfaceGroup(at:)`](./interfacegroup%28at%29.md) and [`interfaceGroup(for:)`](./interfacegroup%28for%29.md) methods on an [`TKSmartCardATR`](../tksmartcardatr.md) object.

## Topics

### Accessing Interface Group Protocol and Bytes
- [var `protocol`: NSNumber?](./interfacegroup/protocol.md)
  The protocol for this group.
- [var ta: NSNumber?](./interfacegroup/ta.md)
  The TA interface byte of ATR group, or `nil` if TA is not present.
- [var tb: NSNumber?](./interfacegroup/tb.md)
  The TB interface byte of ATR group, or `nil` if TB is not present.
- [var tc: NSNumber?](./interfacegroup/tc.md)
  The TC interface byte of ATR group, or `nil` if TC is not present.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Retrieving Interface Groups
- [func interfaceGroup(at: Int) -> TKSmartCardATR.InterfaceGroup?](./interfacegroup%28at%29.md)
  Returns the interface group at the specified index.
- [func interfaceGroup(for: TKSmartCardProtocol) -> TKSmartCardATR.InterfaceGroup?](./interfacegroup%28for%29.md)
  Returns the interface group with the specified protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/interfacegroup)*