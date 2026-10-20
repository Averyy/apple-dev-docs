# fragmentBindings

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

An array of binding instances, each of which represents a parameter of the pipeline state’s fragment shader.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var fragmentBindings: [any MTLBinding] { get }
```

```objc
@property (readonly, nonnull) NSArray<id<MTLBinding>> * fragmentBindings;
```

#### Discussion

The [`MTLBinding`](../mtlbinding.md) elements in the array are in the same order as the fragment shader’s declaration signature.

## See Also

### Inspecting a shader’s parameter
- [var meshBindings: [any MTLBinding]](./meshbindings.md)
  An array of binding instances, each of which represents a parameter of the pipeline state’s mesh shader.
- [var objectBindings: [any MTLBinding]](./objectbindings.md)
  An array of binding instances, each of which represents a parameter of the pipeline state’s object shader.
- [var tileBindings: [any MTLBinding]](./tilebindings.md)
  An array of binding instances, each of which represents a parameter of the pipeline state’s tile shader.
- [var vertexBindings: [any MTLBinding]](./vertexbindings.md)
  An array of binding instances, each of which represents a parameter of the pipeline state’s vertex shader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinereflection/fragmentbindings)*