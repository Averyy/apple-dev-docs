# IP

**Framework**: Network  
**Kind**: struct

The system definition of the Internet Protocol (IP).

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct IP
```

#### Overview

Can be used to insert IP into a protocol stack.

> **Note**: Specifying IP is optional, and need only be included in a protocol stack when configuring IP options.

## Topics

### Initializers
- [init()](ip/init.md)
### Instance Methods
- [func fragmentationDisabled(Bool) -> IP](ip/fragmentationdisabled(_:).md)
  Configure IP to disable fragmentation on outgoing packets.
- [func hopLimit(UInt8) -> IP](ip/hoplimit(_:).md)
  Configure the IP hop limit.
- [func localAddressPreference(NWProtocolIP.Options.AddressPreference) -> IP](ip/localaddresspreference(_:).md)
  Specify a preference selecting the local addresses to use with outbound connections.
- [func minimumMTU(Bool) -> IP](ip/minimummtu(_:).md)
  Configure IP to use the minimum MTU value.
- [func multicastLoopbackDisabled(Bool) -> IP](ip/multicastloopbackdisabled(_:).md)
  Specify if multicast packets should be looped back for local delivery.
- [func receiveTimeCalculated(Bool) -> IP](ip/receivetimecalculated(_:).md)
  Configure IP to calculate receive time for inbound packets.
- [func version(NWProtocolIP.Options.Version) -> IP](ip/version(_:).md)
  Specify a single version of the Internet Protocol to allow.

## Relationships

### Conforms To
- [NetworkProtocolOptions](networkprotocoloptions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/ip)*