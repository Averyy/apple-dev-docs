# init(addresses:networkPrefixLengths:)

**Framework**: Network Extension  
**Kind**: init

Initializes the IPv6 settings object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
init(addresses: [String], networkPrefixLengths: [NSNumber])
```

#### Return Value

The initialized `NEIPv6Settings` object.

## Parameters

- `addresses`: An array of IPv6 address strings. These IPv6 addresses will be assigned to the tunnel’s TUN interface.
- `networkPrefixLengths`: An array of IPv6 network prefix lengths. Each prefix length in this array is combined with the IP address in the corresponding index in   to specify an IPv6 network that the TUN interface is (virtually) connected to. Each prefix length must be set to an integer between 0 and 128.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neipv6settings/init(addresses:networkprefixlengths:))*