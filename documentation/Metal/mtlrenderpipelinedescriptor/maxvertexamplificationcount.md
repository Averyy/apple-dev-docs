# maxVertexAmplificationCount

**Framework**: Metal  
**Kind**: property

The maximum vertex amplification count you can set when encoding render commands.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var maxVertexAmplificationCount: Int { get set }
```

## Mentions

- [Improving Rendering Performance with Vertex Amplification](improving-rendering-performance-with-vertex-amplification.md)

#### Discussion

Before setting this property, call the [`supportsVertexAmplificationCount(_:)`](mtldevice/supportsvertexamplificationcount(_:).md) method on the device object to determine whether that amplification count is supported.

## See Also

- [func setVertexAmplificationCount(Int, viewMappings: UnsafePointer<MTLVertexAmplificationViewMapping>?)](mtlrendercommandencoder/setvertexamplificationcount(_:viewmappings:).md)
  Configures the number of output vertices the render pipeline produces for each input vertex, optionally with render target and viewport offsets.
- [func supportsVertexAmplificationCount(Int) -> Bool](mtldevice/supportsvertexamplificationcount(_:).md)
  Returns a Boolean value that indicates whether the GPU supports an amplification factor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/maxvertexamplificationcount)*