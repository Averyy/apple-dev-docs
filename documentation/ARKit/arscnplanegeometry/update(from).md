# update(from:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Reshapes the SceneKit geometry to match the specified plane mesh.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+

## Declaration

```swift
func update(from planeGeometry: ARPlaneGeometry)
```

```objc
- (void) updateFromPlaneGeometry:(ARPlaneGeometry *) planeGeometry;
```

## Discussion

To update a SceneKit model of a plane actively tracked in an AR session, call this method in your [`ARSCNViewDelegate`](../arscnviewdelegate.md) object’s [`renderer(_:didUpdate:for:)`](../arscnviewdelegate/renderer%28_,didupdate,for%29.md) callback, passing the [`geometry`](../arplaneanchor/geometry.md) property from the [`ARPlaneAnchor`](../arplaneanchor.md) object that callback provides.

## Parameters

- `planeGeometry`: A coarse mesh representation of a detected plane’s estimated shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arscnplanegeometry/update(from:))*