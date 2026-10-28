# SCNetworkProtocolSetConfiguration(_:_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Stores the configuration settings for the specified network protocol.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func SCNetworkProtocolSetConfiguration(_ protocol: SCNetworkProtocol, _ config: CFDictionary?) -> Bool
```

```c
Boolean SCNetworkProtocolSetConfiguration(SCNetworkProtocolRef protocol, CFDictionaryRef config);
```

## Return Value

`TRUE` if the configuration was stored; `FALSE` if an error occurred.

## Parameters

- `protocol`: The network protocol.
- `config`: The configuration settings to store.

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
- [func SCNetworkProtocolSetEnabled(SCNetworkProtocol, Bool) -> Bool](./scnetworkprotocolsetenabled%28_,_%29.md)
  Enables or disables the specified protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkprotocolsetconfiguration(_:_:))*