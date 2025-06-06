# NWProtocolIP.Options

**Framework**: Network  
**Kind**: class

A container of options for configuring how IP is used on a connection.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class Options
```

## Topics

### Selecting an IP Version
- [var version: NWProtocolIP.Options.Version](nwprotocolip/options/version-swift.property.md)
  A required IP version that disables all other versions for a connection.
- [NWProtocolIP.Options.Version](nwprotocolip/options/version-swift.enum.md)
  IP versions to require on connections and listeners.
### Customizing IP Behavior
- [var shouldCalculateReceiveTime: Bool](nwprotocolip/options/shouldcalculatereceivetime.md)
  A Boolean that indicates whether a connection delivers receive timestamps for IP packets.
- [var hopLimit: UInt8](nwprotocolip/options/hoplimit.md)
  The default hop limit for packets a connection generates.
- [var useMinimumMTU: Bool](nwprotocolip/options/useminimummtu.md)
  A Boolean indicating that the connection uses the  minimum MTU value, which is 1280 bytes for IPv6.
- [var disableFragmentation: Bool](nwprotocolip/options/disablefragmentation.md)
  A Boolean that indicates whether fragmentation is disabled on outbound packets.
### Instance Properties
- [var disableMulticastLoopback: Bool](nwprotocolip/options/disablemulticastloopback.md)
- [var localAddressPreference: NWProtocolIP.Options.AddressPreference](nwprotocolip/options/localaddresspreference.md)
### Enumerations
- [NWProtocolIP.Options.AddressPreference](nwprotocolip/options/addresspreference.md)

## Relationships

### Inherits From
- [NWProtocolOptions](nwprotocoloptions.md)
### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [static let definition: NWProtocolDefinition](nwprotocolip/definition.md)
  The system definition of the Internet Protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolip/options)*