# description

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

A textual representation of this object tracking provider.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
final var description: String { get }
```

## See Also

### Inspecting an object-tracking provider
- [var state: DataProviderState](./state.md)
  The state of an object-tracking provider.
- [var allAnchors: [ObjectAnchor]](./allanchors.md)
  An array of all the object anchors the object-tracking provider is tracking.
- [var anchorUpdates: AnchorUpdateSequence<ObjectAnchor>](./anchorupdates.md)
  An asynchronous sequence of anchors the framework updates.
- [ObjectTrackingProvider.Error](./error.md)
  Values that represent an object-tracking error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/objecttrackingprovider/description)*