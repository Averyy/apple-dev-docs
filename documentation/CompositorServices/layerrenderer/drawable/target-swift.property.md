# target

**Framework**: Compositor Services  
**Kind**: property  
**Role**: Instance Property

Returns a value that indicates the target of the drawable type.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var target: LayerRenderer.Drawable.Target { get }
```

```c
cp_drawable_target cp_drawable_get_target(cp_drawable_t drawable);
```

#### Discussion

When drawing for the drawable this can be used to alter what is rendered for different targets. Renderer should always prioritize [`LayerRenderer.Drawable.Target.builtIn`](./target-swift.enum/builtin.md) target type.

## See Also

### Retrieving the target
- [LayerRenderer.Drawable.Target](./target-swift.enum.md)
  The target where the drawable will be displayed/used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/target-swift.property)*