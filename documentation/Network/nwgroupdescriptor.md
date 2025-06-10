# NWGroupDescriptor

**Framework**: Network  
**Kind**: protocol

A protocol that defines a group of endpoints with which you can communicate, such as a multicast group.

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
protocol NWGroupDescriptor : AnyObject, Sendable
```

## Topics

### Inspecting Groups
- [var members: [NWEndpoint]](nwgroupdescriptor/members.md)
  The set of endpoints that define the connection group.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [NWMulticastGroup](nwmulticastgroup.md)
- [NWMultiplexGroup](nwmultiplexgroup.md)

## See Also

- [init(with: any NWGroupDescriptor, using: NWParameters)](nwconnectiongroup/init(with:using:).md)
  Initializes a new connection group with a group identifier.
- [class NWMulticastGroup](nwmulticastgroup.md)
  A descriptor for a group you use to join an IP multicast group on a local network.
- [func start(queue: DispatchQueue)](nwconnectiongroup/start(queue:).md)
  Joins the group, registers to receive messages, and sets the queue on you handle group events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwgroupdescriptor)*