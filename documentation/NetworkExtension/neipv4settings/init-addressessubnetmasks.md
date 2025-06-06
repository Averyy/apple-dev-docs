# init(addresses:subnetMasks:)

**Framework**: Network Extension  
**Kind**: init

Initializes an IPv4 settings object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
init(addresses: [String], subnetMasks: [String])
```

#### Return Value

The initialized NEIPv4Settings object.

## Parameters

- `addresses`: An array of IPv4 address strings. These IPv4 addresses will be assigned to the tunnel’s TUN interface.
- `subnetMasks`: An array of IPv4 network mask strings. Each mask in this array is combined with the IP address in the corresponding index in   to specify an IPv4 network that the TUN interface is (virtually) connected to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neipv4settings/init(addresses:subnetmasks:))*