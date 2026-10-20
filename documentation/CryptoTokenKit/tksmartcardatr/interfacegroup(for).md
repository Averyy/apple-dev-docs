# interfaceGroup(for:)

**Framework**: CryptoTokenKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (TKSmartCardATRInterfaceGroup *) interfaceGroupForProtocol:(TKSmartCardProtocol) protocol;
```

#### Return Value

The interface group with the specified protocol, or `nil` if none exists.

## Parameters

- `protocol`: The protocol used by the desired interface group.

## See Also

### Retrieving Interface Groups
- [func interfaceGroup(at: Int) -> TKSmartCardATR.InterfaceGroup?](./interfacegroup%28at%29.md)
  Returns the interface group at the specified index.
- [TKSmartCardATR.InterfaceGroup](./interfacegroup.md)
  A single interface-bytes group for a Smart Card ATR (Answer to Reset).


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/interfacegroup(for:))*