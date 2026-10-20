# rendererDelegate

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

An object responsible for rendering custom contents for the node using Metal or OpenGL.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
unowned(unsafe) var rendererDelegate: (any SCNNodeRendererDelegate)? { get set }
```

```objc
@property (nonatomic, assign, nullable) id<SCNNodeRendererDelegate> rendererDelegate;
```

#### Discussion

A renderer delegate is a custom object you provide. When SceneKit would otherwise render the contents of the node, it instead tells your delegate to draw contents for the node.

Typically, you use a node renderer delegate for a node that has no associated geometries, cameras, or lights. Such a node only describes a location in space (and a coordinate system transformed by the node hierarchy containing it), which provides an anchor within the scene for whatever custom drawing you want to perform.

If you instead want to customize the results of SceneKit’s geometry and material rendering, use the [`SCNShadable`](../scnshadable.md) protocol to attach shaders to SceneKit objects.

## See Also

### Customizing Node Rendering
- [var filters: [CIFilter]?](./filters.md)
  An array of Core Image filters to be applied to the rendered contents of the node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnnode/rendererdelegate)*