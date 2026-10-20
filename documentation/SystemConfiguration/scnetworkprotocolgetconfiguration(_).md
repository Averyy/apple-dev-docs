# SCNetworkProtocolGetConfiguration(_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Returns the configuration settings associated with the specified protocol.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func SCNetworkProtocolGetConfiguration(_ protocol: SCNetworkProtocol) -> CFDictionary?
```

```c
CFDictionaryRefSCNetworkProtocolGetConfiguration(SCNetworkProtocolRef protocol);
```

#### Return Value

The configuration settings associated with the protocol, or `NULL` if no configuration settings are associated with the protocol or an error occurred.

## Parameters

- `protocol`: The network protocol.

## See Also

### Configuring Network Protocols
- [func SCNetworkProtocolGetEnabled(SCNetworkProtocol) -> Bool](./scnetworkprotocolgetenabled%28_%29.md)
  Returns a Boolean value indicating whether the specified protocol is enabled.
- [func SCNetworkProtocolGetProtocolType(SCNetworkProtocol) -> CFString?](./scnetworkprotocolgetprotocoltype%28_%29.md)
  Returns the type of the specified network protocol.
- [func SCNetworkProtocolGetTypeID() -> CFTypeID](./scnetworkprotocolgettypeid%28%29.md)
  Returns the type identifier of all `SCNetworkProtocol` instances.
- [func SCNetworkProtocolSetConfiguration(SCNetworkProtocol, CFDictionary?) -> Bool](./scnetworkprotocolsetconfiguration%28_,_%29.md)
  Stores the configuration settings for the specified network protocol.
- [func SCNetworkProtocolSetEnabled(SCNetworkProtocol, Bool) -> Bool](./scnetworkprotocolsetenabled%28_,_%29.md)
  Enables or disables the specified protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkprotocolgetconfiguration(_:))*