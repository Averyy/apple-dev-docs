# AccessorySensorUpdates.Update

**Framework**: AudioAccessoryKit  
**Kind**: enum

A single update emitted by the stream.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
enum Update
```

## Topics

### Enumeration Cases
- [AccessorySensorUpdates.Update.malformedPacket](accessorysensorupdates/update/malformedpacket.md)
  A malformed packet was received; the connection remains open and subsequent packets may still be valid.
- [AccessorySensorUpdates.Update.packet(_:)](accessorysensorupdates/update/packet(_:).md)
  A valid sensor data packet from the accessory.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audioaccessorykit/accessorysensorupdates/update)*