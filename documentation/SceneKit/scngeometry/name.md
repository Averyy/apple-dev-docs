# name

**Framework**: SceneKit  
**Kind**: property

A name associated with the geometry object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var name: String? { get set }
```

#### Discussion

You can provide a descriptive name for a geometry object to make managing your scene graph easier. Geometries loaded from a scene file may have names assigned by an artist using a 3D authoring tool. Use the [`SCNSceneSource`](scnscenesource.md) class to examine geometries in a scene file without loading its scene graph.

Geometry names are saved when you export a scene to a file using its [`write(to:options:delegate:progressHandler:)`](scnscene/write(to:options:delegate:progresshandler:).md) method. They also appear in the Xcode scene editor.

## See Also

- [protocol SCNBoundingVolume](scnboundingvolume.md)
  Methods common to the [`SCNNode`](scnnode.md) and [`SCNGeometry`](scngeometry.md) classes for measuring location and size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scngeometry/name)*