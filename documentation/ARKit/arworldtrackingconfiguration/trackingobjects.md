# trackingObjects

**Framework**: ARKit  
**Kind**: property

Objects to track in the scene.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
var trackingObjects: Set<ARReferenceObject> { get set }
```

#### Discussion

If set, the session will attempt to track the specified objects. When an object is detected an `ARObjectAnchor` will be added to the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arworldtrackingconfiguration/trackingobjects)*