# interfaceGroup(at:)

**Framework**: CryptoTokenKit  
**Kind**: method

Returns the interface group at the specified index.

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
func interfaceGroup(at index: Int) -> TKSmartCardATR.InterfaceGroup?
```

#### Return Value

The interface group at the specified index, or `nil` if not present.

## Parameters

- `index`: The index of the desired interface group.

## See Also

- [func interfaceGroup(for: TKSmartCardProtocol) -> TKSmartCardATR.InterfaceGroup?](tksmartcardatr/interfacegroup(for:).md)
  Returns the interface group with the specified protocol.
- [TKSmartCardATR.InterfaceGroup](tksmartcardatr/interfacegroup.md)
  A single interface-bytes group for a Smart Card ATR (Answer to Reset).


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/interfacegroup(at:))*