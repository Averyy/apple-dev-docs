# target

**Framework**: Compositor Services  
**Kind**: property

Returns a value that indicates the target of the drawable type.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var target: LayerRenderer.Drawable.Target { get }
```

#### Discussion

When drawing for the drawable this can be used to alter what is rendered for different targets. Renderer should always prioritize [`LayerRenderer.Drawable.Target.builtIn`](layerrenderer/drawable/target-swift.enum/builtin.md) target type.

## See Also

- [LayerRenderer.Drawable.Target](layerrenderer/drawable/target-swift.enum.md)
  The target where the drawable will be displayed/used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/target-swift.property)*