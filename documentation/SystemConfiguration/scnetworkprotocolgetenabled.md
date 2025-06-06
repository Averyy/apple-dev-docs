# SCNetworkProtocolGetEnabled(_:)

**Framework**: System Configuration  
**Kind**: func

Returns a Boolean value indicating whether the specified protocol is enabled.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func SCNetworkProtocolGetEnabled(_ protocol: SCNetworkProtocol) -> Bool
```

#### Return Value

`TRUE` if the protocol is enabled; otherwise, `FALSE`.

## Parameters

- `protocol`: The network protocol.

## See Also

- [func SCNetworkProtocolGetConfiguration(SCNetworkProtocol) -> CFDictionary?](scnetworkprotocolgetconfiguration(_:).md)
  Returns the configuration settings associated with the specified protocol.
- [func SCNetworkProtocolGetProtocolType(SCNetworkProtocol) -> CFString?](scnetworkprotocolgetprotocoltype(_:).md)
  Returns the type of the specified network protocol.
- [func SCNetworkProtocolGetTypeID() -> CFTypeID](scnetworkprotocolgettypeid().md)
  Returns the type identifier of all `SCNetworkProtocol` instances.
- [func SCNetworkProtocolSetConfiguration(SCNetworkProtocol, CFDictionary?) -> Bool](scnetworkprotocolsetconfiguration(_:_:).md)
  Stores the configuration settings for the specified network protocol.
- [func SCNetworkProtocolSetEnabled(SCNetworkProtocol, Bool) -> Bool](scnetworkprotocolsetenabled(_:_:).md)
  Enables or disables the specified protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkprotocolgetenabled(_:))*