# SCNetworkProtocolGetConfiguration(_:)

**Framework**: System Configuration  
**Kind**: func

Returns the configuration settings associated with the specified protocol.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func SCNetworkProtocolGetConfiguration(_ protocol: SCNetworkProtocol) -> CFDictionary?
```

#### Return Value

The configuration settings associated with the protocol, or `NULL` if no configuration settings are associated with the protocol or an error occurred.

## Parameters

- `protocol`: The network protocol.

## See Also

- [func SCNetworkProtocolGetEnabled(SCNetworkProtocol) -> Bool](scnetworkprotocolgetenabled(_:).md)
  Returns a Boolean value indicating whether the specified protocol is enabled.
- [func SCNetworkProtocolGetProtocolType(SCNetworkProtocol) -> CFString?](scnetworkprotocolgetprotocoltype(_:).md)
  Returns the type of the specified network protocol.
- [func SCNetworkProtocolGetTypeID() -> CFTypeID](scnetworkprotocolgettypeid().md)
  Returns the type identifier of all `SCNetworkProtocol` instances.
- [func SCNetworkProtocolSetConfiguration(SCNetworkProtocol, CFDictionary?) -> Bool](scnetworkprotocolsetconfiguration(_:_:).md)
  Stores the configuration settings for the specified network protocol.
- [func SCNetworkProtocolSetEnabled(SCNetworkProtocol, Bool) -> Bool](scnetworkprotocolsetenabled(_:_:).md)
  Enables or disables the specified protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkprotocolgetconfiguration(_:))*