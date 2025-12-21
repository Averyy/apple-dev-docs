# interfaceGroup(for:)

**Framework**: CryptoTokenKit  
**Kind**: method

Returns the interface group with the specified protocol.

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
func interfaceGroup(for protocol: TKSmartCardProtocol) -> TKSmartCardATR.InterfaceGroup?
```

#### Return Value

The interface group with the specified protocol, or `nil` if none exists.

## Parameters

- `protocol`: The protocol used by the desired interface group.

## See Also

- [func interfaceGroup(at: Int) -> TKSmartCardATR.InterfaceGroup?](tksmartcardatr/interfacegroup(at:).md)
  Returns the interface group at the specified index.
- [TKSmartCardATR.InterfaceGroup](tksmartcardatr/interfacegroup.md)
  A single interface-bytes group for a Smart Card ATR (Answer to Reset).


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/interfacegroup(for:))*