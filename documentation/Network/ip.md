# IP

**Framework**: Network  
**Kind**: struct  
**Role**: Structure

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

## Overview

Can be used to insert IP into a protocol stack.

> **Note**: Specifying IP is optional, and need only be included in a protocol stack when configuring IP options.

## Topics

### Initializers
- [init()](./ip/init%28%29.md)
### Instance Methods
- [func fragmentationDisabled(Bool) -> IP](./ip/fragmentationdisabled%28_%29.md)
  Configure IP to disable fragmentation on outgoing packets.
- [func hopLimit(UInt8) -> IP](./ip/hoplimit%28_%29.md)
  Configure the IP hop limit.
- [func localAddressPreference(NWProtocolIP.Options.AddressPreference) -> IP](./ip/localaddresspreference%28_%29.md)
- [func minimumMTU(Bool) -> IP](./ip/minimummtu%28_%29.md)
  Configure IP to use the minimum MTU value.
- [func multicastLoopbackDisabled(Bool) -> IP](./ip/multicastloopbackdisabled%28_%29.md)
  Specify if multicast packets should be looped back for local delivery.
- [func receiveTimeCalculated(Bool) -> IP](./ip/receivetimecalculated%28_%29.md)
  Configure IP to calculate receive time for inbound packets.
- [func version(NWProtocolIP.Options.Version) -> IP](./ip/version%28_%29.md)

## Relationships

### Conforms To
- [NetworkProtocolOptions](./networkprotocoloptions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/ip)*