# NWMulticastGroup

**Framework**: Network  
**Kind**: class

A descriptor for a group you use to join an IP multicast group on a local network.

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
class NWMulticastGroup
```

#### Overview

> ❗ **Important**:  In order to use multicast on iOS, your app will need to have the `com.apple.developer.networking.multicast` entitlement.

 In order to use multicast on iOS, your app will need to have the `com.apple.developer.networking.multicast` entitlement.

## Topics

### Essentials
- [com.apple.developer.networking.multicast](../BundleResources/Entitlements/com.apple.developer.networking.multicast.md)
  A Boolean value that indicates whether an app can send or receive IP multicast traffic.
### Defining Multicast Groups
- [init(for: [NWEndpoint], from: NWEndpoint?, disableUnicast: Bool) throws](nwmulticastgroup/init(for:from:disableunicast:).md)
  Initializes a multicast group with a set of multicast addresses.
### Inspecting Multicast Groups
- [var members: [NWEndpoint]](nwmulticastgroup/members.md)
  The set of IP multicast group addresses that the connection group joins.
- [let sourceFilter: NWEndpoint?](nwmulticastgroup/sourcefilter.md)
  An optional address endpoint you provide to filter received multicast packets.
- [let isUnicastDisabled: Bool](nwmulticastgroup/isunicastdisabled.md)
  A Boolean that specifies whether the connection group rejects unicast traffic.

## Relationships

### Conforms To
- [NWGroupDescriptor](nwgroupdescriptor.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [init(with: any NWGroupDescriptor, using: NWParameters)](nwconnectiongroup/init(with:using:).md)
  Initializes a new connection group with a group identifier.
- [protocol NWGroupDescriptor](nwgroupdescriptor.md)
  A protocol that defines a group of endpoints with which you can communicate, such as a multicast group.
- [func start(queue: DispatchQueue)](nwconnectiongroup/start(queue:).md)
  Joins the group, registers to receive messages, and sets the queue on you handle group events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwmulticastgroup)*