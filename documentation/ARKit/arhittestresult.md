# ARHitTestResult

**Framework**: ARKit  
**Kind**: class  
**Role**: Class

Information about a real-world surface found by examining a point on the screen.

**Availability**:
- iOS 11.0+ - Deprecated in 14.0
- iPadOS 11.0+ - Deprecated in 14.0

> **Deprecated**: Use raycasting

## Declaration

```swift
class ARHitTestResult
```

```objc
@interface ARHitTestResult : NSObject
```

## Overview

If you use SceneKit or SpriteKit as your renderer, you can search for real-world surfaces at a screen point using:

- [`ARSCNView`](./arscnview.md) [`hitTest(_:types:)`](./arscnview/hittest%28_,types%29.md)
- [`ARSKView`](./arskview.md) [`hitTest(_:types:)`](./arskview/hittest%28_,types%29.md)

Otherwise, you can search the camera image for real-world content using the [`ARFrame`](./arframe.md) [`hitTest(_:types:)`](./arframe/hittest%28_,types%29.md) method. Because a frame is independent of a view, for this method you pass a point specified in normalized image coordinates (where `(0,0)` is the top left corner of the image and `(1,1)` is the lower right).

All these methods return an array of [`ARHitTestResult`](./arhittestresult.md) objects describing the content found. The number and order of results in the array depends on the search types you specify and the order you specify them in. For example, consider the code below:

```swift
let results = view.hitTest(point, [.existingPlaneUsingGeometry, .estimatedHorizontalPlane])
```

This [`hitTest(_:types:)`](./arscnview/hittest%28_,types%29.md) call searches first for plane anchors already present in the session (according to the session configuration’s [`planeDetection`](./arworldtrackingconfiguration/planedetection-swift.property.md) settings); returning any such results (in order of distance from the camera) as the first elements in the array. This call also (due to the [`estimatedHorizontalPlane`](./arhittestresult/resulttype/estimatedhorizontalplane.md) request) attempts to determine whether the hit test ray intersects any horizontal surface not already found by plane detection, and returns that result (if any) as the last element in the array.

## Topics

### Identifying Results
- [var type: ARHitTestResult.ResultType](./arhittestresult/type.md)
  The kind of detected feature the search result represents.
- [ARHitTestResult.ResultType](./arhittestresult/resulttype.md)
  Possible types for specifying a hit-test search, or for the result of a hit-test search.
- [var anchor: ARAnchor?](./arhittestresult/anchor.md)
  The anchor representing the detected surface, if any.
### Examining Result Geometry
- [var distance: CGFloat](./arhittestresult/distance.md)
  The distance, in meters, from the camera to the detected surface.
- [var worldTransform: simd_float4x4](./arhittestresult/worldtransform.md)
  The position and orientation of the result relative to the world coordinate system.
- [var localTransform: simd_float4x4](./arhittestresult/localtransform.md)
  The position and orientation of the result relative to the nearest anchor or feature point.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arhittestresult)*