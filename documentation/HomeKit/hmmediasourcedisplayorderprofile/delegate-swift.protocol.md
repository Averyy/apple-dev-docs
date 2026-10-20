# HMMediaSourceDisplayOrderProfile.Delegate

**Framework**: HomeKit  
**Kind**: protocol  
**Role**: Protocol

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
- [func mediaSourceDisplayOrderProfileDidUpdateOrder(HMMediaSourceDisplayOrderProfile)](./delegate-swift.protocol/mediasourcedisplayorderprofiledidupdateorder%28_%29.md)
  Informs the delegate when the system modifies the media source display order.

## Relationships

### Inherits From
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing input source order
- [func writeOrder([Int]) async throws](./writeorder%28_%29.md)
  Writes the display order of the media sources to the accessory.
- [var delegate: (any HMMediaSourceDisplayOrderProfile.Delegate)?](./delegate-swift.property.md)
  The property that handles updates to the display order.
- [var order: [Int]](./order.md)
  The display order of input media sources.
- [let canModifyOrder: Bool](./canmodifyorder.md)
  A Boolean that indicates if the display order of the input media sources can be modified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmmediasourcedisplayorderprofile/delegate-swift.protocol)*