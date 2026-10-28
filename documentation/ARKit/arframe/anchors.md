# anchors

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The list of anchors representing positions tracked or objects detected in the scene.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
var anchors: [ARAnchor] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<__kindof ARAnchor *> * anchors;
```

## Discussion

You can manually add or remove anchors to track locations in the scene using the [`ARSession`](../arsession.md) class. Depending on session configuration, ARKit may also add anchors, such as the origin of the world coordinate system or automatically detected planes.

## See Also

### Tracking and interacting with the real world
- [func raycastQuery(from: CGPoint, allowing: ARRaycastQuery.Target, alignment: ARRaycastQuery.TargetAlignment) -> ARRaycastQuery](./raycastquery%28from,allowing,alignment%29.md)
  Get a ray-cast query for a screen point.
- [func hitTest(CGPoint, types: ARHitTestResult.ResultType) -> [ARHitTestResult]](./hittest%28_,types%29.md)
  Searches for real-world objects or AR anchors in the captured camera image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arframe/anchors)*