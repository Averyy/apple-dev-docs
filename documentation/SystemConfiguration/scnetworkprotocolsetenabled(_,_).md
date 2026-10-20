# SCNetworkProtocolSetEnabled(_:_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Enables or disables the specified protocol.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func SCNetworkProtocolSetEnabled(_ protocol: SCNetworkProtocol, _ enabled: Bool) -> Bool
```

```c
Boolean SCNetworkProtocolSetEnabled(SCNetworkProtocolRef protocol, Boolean enabled);
```

#### Return Value

`TRUE` if the enabled status was saved; `FALSE` if an error occurred.

## Parameters

- `protocol`: The network protocol to enable or disable.
- `enabled`: `TRUE` if the protocol should be enabled.

## See Also

### Configuring Network Protocols
- [func SCNetworkProtocolGetConfiguration(SCNetworkProtocol) -> CFDictionary?](./scnetworkprotocolgetconfiguration%28_%29.md)
  Returns the configuration settings associated with the specified protocol.
- [func SCNetworkProtocolGetEnabled(SCNetworkProtocol) -> Bool](./scnetworkprotocolgetenabled%28_%29.md)
  Returns a Boolean value indicating whether the specified protocol is enabled.
- [func SCNetworkProtocolGetProtocolType(SCNetworkProtocol) -> CFString?](./scnetworkprotocolgetprotocoltype%28_%29.md)
  Returns the type of the specified network protocol.
- [func SCNetworkProtocolGetTypeID() -> CFTypeID](./scnetworkprotocolgettypeid%28%29.md)
  Returns the type identifier of all `SCNetworkProtocol` instances.
- [func SCNetworkProtocolSetConfiguration(SCNetworkProtocol, CFDictionary?) -> Bool](./scnetworkprotocolsetconfiguration%28_,_%29.md)
  Stores the configuration settings for the specified network protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkprotocolsetenabled(_:_:))*