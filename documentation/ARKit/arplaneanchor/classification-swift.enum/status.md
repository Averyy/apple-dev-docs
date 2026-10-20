# ARPlaneAnchor.Classification.Status

**Framework**: ARKit  
**Kind**: enum  
**Role**: Enumeration

Reasons ARKit is unable to classify a plane.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+

## Declaration

```swift
enum Status
```

#### Overview

[`ARPlaneAnchor.Classification.Status`](./status.md) tells you why a plane anchor’s [`classification`](../classification-2r4x8.md) is [`ARPlaneAnchor.Classification.none(_:)`](./none%28_%29.md).

## Topics

### Classification Status
- [ARPlaneAnchor.Classification.Status.notAvailable](./status/notavailable.md)
  ARKit cannot currently provide plane classification information.
- [ARPlaneAnchor.Classification.Status.undetermined](./status/undetermined.md)
  ARKit has not yet produced a classification for the plane anchor.
- [ARPlaneAnchor.Classification.Status.unknown](./status/unknown.md)
  ARKit has completed its classification process for the plane anchor, but the result is inconclusive.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Missing Classification Status
- [case none(ARPlaneAnchor.Classification.Status)](./none%28_%29.md)
  No classification is available for the plane anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arplaneanchor/classification-swift.enum/status)*