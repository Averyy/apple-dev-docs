# allAnchors

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

An array of all the object anchors the object-tracking provider is tracking.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
final var allAnchors: [ObjectAnchor] { get }
```

## See Also

### Inspecting an object-tracking provider
- [var state: DataProviderState](./state.md)
  The state of an object-tracking provider.
- [var anchorUpdates: AnchorUpdateSequence<ObjectAnchor>](./anchorupdates.md)
  An asynchronous sequence of anchors the framework updates.
- [ObjectTrackingProvider.Error](./error.md)
  Values that represent an object-tracking error.
- [var description: String](./description.md)
  A textual representation of this object tracking provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/objecttrackingprovider/allanchors)*