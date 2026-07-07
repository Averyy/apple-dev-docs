# trackingObjects

**Framework**: ARKit  
**Kind**: property

Objects to track in the scene.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
var trackingObjects: Set<ARReferenceObject> { get set }
```

#### Discussion

The system tracks the object at the full frame rate of the selected `videoFormat`. When an object is tracked, an `ARObjectAnchor` is added to the session.

Use this property for moving or handheld objects that require precise, per-frame pose updates. High frame-rate tracking significantly increases power consumption and processing load. For mostly stationary objects, use `detectionObjects` instead.

> **Note**: Only the `.referenceobject` format (introduced in iOS 27) is supported; the older `.arobject` format works only with `detectionObjects`. A single session can’t use both formats.

## See Also

- [var detectionObjects: Set<ARReferenceObject>](argeotrackingconfiguration/detectionobjects.md)
  A set of 3D objects that the framework attempts to detect in the user’s environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeotrackingconfiguration/trackingobjects)*