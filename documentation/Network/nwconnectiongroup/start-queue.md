# start(queue:)

**Framework**: Network  
**Kind**: method

Joins the group, registers to receive messages, and sets the queue on you handle group events.

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
final func start(queue: DispatchQueue)
```

## See Also

- [init(with: any NWGroupDescriptor, using: NWParameters)](nwconnectiongroup/init(with:using:).md)
  Initializes a new connection group with a group identifier.
- [class NWMulticastGroup](nwmulticastgroup.md)
  A descriptor for a group you use to join an IP multicast group on a local network.
- [protocol NWGroupDescriptor](nwgroupdescriptor.md)
  A protocol that defines a group of endpoints with which you can communicate, such as a multicast group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnectiongroup/start(queue:))*