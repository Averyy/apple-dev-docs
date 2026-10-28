# SCNetworkProtocolGetTypeID()

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Returns the type identifier of all `SCNetworkProtocol` instances.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func SCNetworkProtocolGetTypeID() -> CFTypeID
```

```c
CFTypeID SCNetworkProtocolGetTypeID();
```

## Return Value

The type identifier of all `SCNetworkProtocol` instances.

## See Also

### Configuring Network Protocols
- [func SCNetworkProtocolGetConfiguration(SCNetworkProtocol) -> CFDictionary?](./scnetworkprotocolgetconfiguration%28_%29.md)
  Returns the configuration settings associated with the specified protocol.
- [func SCNetworkProtocolGetEnabled(SCNetworkProtocol) -> Bool](./scnetworkprotocolgetenabled%28_%29.md)
  Returns a Boolean value indicating whether the specified protocol is enabled.
- [func SCNetworkProtocolGetProtocolType(SCNetworkProtocol) -> CFString?](./scnetworkprotocolgetprotocoltype%28_%29.md)
  Returns the type of the specified network protocol.
- [func SCNetworkProtocolSetConfiguration(SCNetworkProtocol, CFDictionary?) -> Bool](./scnetworkprotocolsetconfiguration%28_,_%29.md)
  Stores the configuration settings for the specified network protocol.
- [func SCNetworkProtocolSetEnabled(SCNetworkProtocol, Bool) -> Bool](./scnetworkprotocolsetenabled%28_,_%29.md)
  Enables or disables the specified protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkprotocolgettypeid())*