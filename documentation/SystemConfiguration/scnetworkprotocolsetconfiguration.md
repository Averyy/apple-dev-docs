# SCNetworkProtocolSetConfiguration(_:_:)

**Framework**: System Configuration  
**Kind**: func

Stores the configuration settings for the specified network protocol.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func SCNetworkProtocolSetConfiguration(_ protocol: SCNetworkProtocol, _ config: CFDictionary?) -> Bool
```

#### Return Value

`TRUE` if the configuration was stored; `FALSE` if an error occurred.

## Parameters

- `protocol`: The network protocol.
- `config`: The configuration settings to store.

## See Also

- [func SCNetworkProtocolGetConfiguration(SCNetworkProtocol) -> CFDictionary?](scnetworkprotocolgetconfiguration(_:).md)
  Returns the configuration settings associated with the specified protocol.
- [func SCNetworkProtocolGetEnabled(SCNetworkProtocol) -> Bool](scnetworkprotocolgetenabled(_:).md)
  Returns a Boolean value indicating whether the specified protocol is enabled.
- [func SCNetworkProtocolGetProtocolType(SCNetworkProtocol) -> CFString?](scnetworkprotocolgetprotocoltype(_:).md)
  Returns the type of the specified network protocol.
- [func SCNetworkProtocolGetTypeID() -> CFTypeID](scnetworkprotocolgettypeid().md)
  Returns the type identifier of all `SCNetworkProtocol` instances.
- [func SCNetworkProtocolSetEnabled(SCNetworkProtocol, Bool) -> Bool](scnetworkprotocolsetenabled(_:_:).md)
  Enables or disables the specified protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkprotocolsetconfiguration(_:_:))*