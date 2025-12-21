# TKSmartCardATR.InterfaceGroup

**Framework**: CryptoTokenKit  
**Kind**: class

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

#### Overview

You access instances of this class by calling the [`interfaceGroup(at:)`](tksmartcardatr/interfacegroup(at:).md) and [`interfaceGroup(for:)`](tksmartcardatr/interfacegroup(for:).md) methods on an [`TKSmartCardATR`](tksmartcardatr.md) object.

## Topics

### Accessing Interface Group Protocol and Bytes
- [var `protocol`: NSNumber?](tksmartcardatr/interfacegroup/protocol.md)
  The protocol for this group.
- [var ta: NSNumber?](tksmartcardatr/interfacegroup/ta.md)
  The TA interface byte of ATR group, or `nil` if TA is not present.
- [var tb: NSNumber?](tksmartcardatr/interfacegroup/tb.md)
  The TB interface byte of ATR group, or `nil` if TB is not present.
- [var tc: NSNumber?](tksmartcardatr/interfacegroup/tc.md)
  The TC interface byte of ATR group, or `nil` if TC is not present.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func interfaceGroup(at: Int) -> TKSmartCardATR.InterfaceGroup?](tksmartcardatr/interfacegroup(at:).md)
  Returns the interface group at the specified index.
- [func interfaceGroup(for: TKSmartCardProtocol) -> TKSmartCardATR.InterfaceGroup?](tksmartcardatr/interfacegroup(for:).md)
  Returns the interface group with the specified protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/interfacegroup)*