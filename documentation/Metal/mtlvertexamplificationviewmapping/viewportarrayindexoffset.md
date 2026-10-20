# viewportArrayIndexOffset

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

An offset into the list of viewports.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var viewportArrayIndexOffset: UInt32
```

```c
uint32_t viewportArrayIndexOffset;
```

## Mentions

- [Improving rendering performance with vertex amplification](../improving-rendering-performance-with-vertex-amplification.md)

#### Discussion

To specify a list of offsets, call the [`setVertexAmplificationCount(_:viewMappings:)`](../mtlrendercommandencoder/setvertexamplificationcount%28_,viewmappings%29.md) method.

When your app renders to different render targets, you specify the render target index to render to in your vertex shader by adding the `viewport_array_index` attribute to one of the vertex shader’s outputs. If you are using vertex amplification, Metal calculates the index for each amplified vertex by adding the index offset for the vertex to the value returned from your shader.

## See Also

### Specifying mapping offsets
- [var renderTargetArrayIndexOffset: UInt32](./rendertargetarrayindexoffset.md)
  An offset into the list of render targets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvertexamplificationviewmapping/viewportarrayindexoffset)*