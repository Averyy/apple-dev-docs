# delegate

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

The property that handles updates to the display order.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
weak var delegate: (any HMMediaSourceDisplayOrderProfile.Delegate)?
```

## See Also

### Managing input source order
- [func writeOrder([Int]) async throws](./writeorder%28_%29.md)
  Writes the display order of the media sources to the accessory.
- [var order: [Int]](./order.md)
  The display order of input media sources.
- [let canModifyOrder: Bool](./canmodifyorder.md)
  A Boolean that indicates if the display order of the input media sources can be modified.
- [HMMediaSourceDisplayOrderProfile.Delegate](./delegate-swift.protocol.md)
  The protocol through which a delegate receives updates on the order of input media sources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmmediasourcedisplayorderprofile/delegate-swift.property)*