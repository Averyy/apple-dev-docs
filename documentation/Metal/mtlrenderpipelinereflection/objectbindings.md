# objectBindings

**Framework**: Metal  
**Kind**: property

An array of binding instances, each of which represents a parameter of the pipeline state’s object shader.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var objectBindings: [any MTLBinding] { get }
```

#### Discussion

The [`MTLBinding`](mtlbinding.md) elements in the array are in the same order as the object shader’s declaration signature.

## See Also

- [var fragmentBindings: [any MTLBinding]](mtlrenderpipelinereflection/fragmentbindings.md)
  An array of binding instances, each of which represents a parameter of the pipeline state’s fragment shader.
- [var meshBindings: [any MTLBinding]](mtlrenderpipelinereflection/meshbindings.md)
  An array of binding instances, each of which represents a parameter of the pipeline state’s mesh shader.
- [var tileBindings: [any MTLBinding]](mtlrenderpipelinereflection/tilebindings.md)
  An array of binding instances, each of which represents a parameter of the pipeline state’s tile shader.
- [var vertexBindings: [any MTLBinding]](mtlrenderpipelinereflection/vertexbindings.md)
  An array of binding instances, each of which represents a parameter of the pipeline state’s vertex shader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinereflection/objectbindings)*