# detectionObjects

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

A set of 3D objects that the framework attempts to detect in the user’s environment.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Declaration

```swift
var detectionObjects: Set<ARReferenceObject> { get set }
```

```objc
@property (nonatomic, copy) NSSet<ARReferenceObject *> * detectionObjects;
```

## Discussion

The system keeps the object’s pose stable in world space, consuming less power. Virtual content stays aligned with the object as long as it doesn’t move; if the object moves, the system may delay the pose update. When an object is detected, an `ARObjectAnchor` is added to the session.

Use this property for objects that are mostly stationary. For moving or handheld objects that need precise, per-frame updates, use `trackingObjects` instead.

> **Note**: Supports both the `.arobject` format (introduced in iOS 12) and the `.referenceobject` format (introduced in iOS 27). A single session can’t use both formats.

## See Also

### Detecting and tracking real-world objects
- [var trackingObjects: Set<ARReferenceObject>](./trackingobjects.md)
  Objects to track in the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeotrackingconfiguration/detectionobjects)*