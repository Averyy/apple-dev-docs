# SCNetworkProtocolGetProtocolType(_:)

**Framework**: System Configuration  
**Kind**: func

Returns the type of the specified network protocol.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func SCNetworkProtocolGetProtocolType(_ protocol: SCNetworkProtocol) -> CFString?
```

#### Return Value

The protocol type.

## Parameters

- `protocol`: The network protocol.

## See Also

- [func SCNetworkProtocolGetConfiguration(SCNetworkProtocol) -> CFDictionary?](scnetworkprotocolgetconfiguration(_:).md)
  Returns the configuration settings associated with the specified protocol.
- [func SCNetworkProtocolGetEnabled(SCNetworkProtocol) -> Bool](scnetworkprotocolgetenabled(_:).md)
  Returns a Boolean value indicating whether the specified protocol is enabled.
- [func SCNetworkProtocolGetTypeID() -> CFTypeID](scnetworkprotocolgettypeid().md)
  Returns the type identifier of all `SCNetworkProtocol` instances.
- [func SCNetworkProtocolSetConfiguration(SCNetworkProtocol, CFDictionary?) -> Bool](scnetworkprotocolsetconfiguration(_:_:).md)
  Stores the configuration settings for the specified network protocol.
- [func SCNetworkProtocolSetEnabled(SCNetworkProtocol, Bool) -> Bool](scnetworkprotocolsetenabled(_:_:).md)
  Enables or disables the specified protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkprotocolgetprotocoltype(_:))*