# init(for:from:disableUnicast:)

**Framework**: Network  
**Kind**: init

Initializes a multicast group with a set of multicast addresses.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(for groupAddresses: [NWEndpoint], from: NWEndpoint? = nil, disableUnicast: Bool = false) throws
```

## Parameters

- `groupAddresses`: A set of multicast address endpoints you specify to define the IP multicast groups to join. The port indicates which local port the connection group will use to receive messages.
- `from`: An optional address endpoint used to filter received multicast packets.
- `disableUnicast`: A Boolean that specifies whether the connection group rejects unicast traffic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwmulticastgroup/init(for:from:disableunicast:))*