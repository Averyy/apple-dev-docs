# HMMediaSourceDisplayOrderProfile.Delegate

**Framework**: HomeKit  
**Kind**: protocol

The protocol through which a delegate receives updates on the order of input media sources.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
protocol Delegate : AnyObject, Sendable
```

## Topics

### Instance Methods
- [func mediaSourceDisplayOrderProfileDidUpdateOrder(HMMediaSourceDisplayOrderProfile)](hmmediasourcedisplayorderprofile/delegate-swift.protocol/mediasourcedisplayorderprofiledidupdateorder(_:).md)
  Informs the delegate when the system modifies the media source display order.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)

## See Also

- [func writeOrder([Int]) async throws](hmmediasourcedisplayorderprofile/writeorder(_:).md)
  Writes the display order of the media sources to the accessory.
- [var delegate: (any HMMediaSourceDisplayOrderProfile.Delegate)?](hmmediasourcedisplayorderprofile/delegate-swift.property.md)
  The property that handles updates to the display order.
- [var order: [Int]](hmmediasourcedisplayorderprofile/order.md)
  The display order of input media sources.
- [let canModifyOrder: Bool](hmmediasourcedisplayorderprofile/canmodifyorder.md)
  A Boolean that indicates if the display order of the input media sources can be modified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmmediasourcedisplayorderprofile/delegate-swift.protocol)*