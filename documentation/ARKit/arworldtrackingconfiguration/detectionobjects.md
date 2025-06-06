# detectionObjects

**Framework**: ARKit  
**Kind**: property

A set of 3D objects that the framework attempts to detect in the user’s environment.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var detectionObjects: Set<ARReferenceObject> { get set }
```

#### Discussion

Use this property to choose known 3D objects for ARKit to find in the user’s environment and present as [`ARObjectAnchor`](arobjectanchor.md) for use in your AR experience.

To create reference objects for detection, scan them in a world-tracking session and use [`ARWorldMap`](arworldmap.md) to extract [`ARReferenceObject`](arreferenceobject.md) instances. You can then save reference objects as files and package them in any ARKit app you create using an Xcode asset catalog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arworldtrackingconfiguration/detectionobjects)*