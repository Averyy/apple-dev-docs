# ARPlaneAnchor.Classification.Status

**Framework**: ARKit  
**Kind**: enum

Reasons ARKit is unable to classify a plane.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+

## Declaration

```swift
enum Status
```

#### Overview

[`ARPlaneAnchor.Classification.Status`](arplaneanchor/classification-swift.enum/status.md) tells you why a plane anchor’s [`classification`](arplaneanchor/classification-2r4x8.md) is [`ARPlaneAnchor.Classification.none(_:)`](arplaneanchor/classification-swift.enum/none(_:).md).

## Topics

### Classification Status
- [ARPlaneAnchor.Classification.Status.notAvailable](arplaneanchor/classification-swift.enum/status/notavailable.md)
  ARKit cannot currently provide plane classification information.
- [ARPlaneAnchor.Classification.Status.undetermined](arplaneanchor/classification-swift.enum/status/undetermined.md)
  ARKit has not yet produced a classification for the plane anchor.
- [ARPlaneAnchor.Classification.Status.unknown](arplaneanchor/classification-swift.enum/status/unknown.md)
  ARKit has completed its classification process for the plane anchor, but the result is inconclusive.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [case none(ARPlaneAnchor.Classification.Status)](arplaneanchor/classification-swift.enum/none(_:).md)
  No classification is available for the plane anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arplaneanchor/classification-swift.enum/status)*