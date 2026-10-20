# maxVertexAmplificationCount

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readwrite) NSUInteger maxVertexAmplificationCount;
```

## Mentions

- [Improving rendering performance with vertex amplification](../improving-rendering-performance-with-vertex-amplification.md)

#### Discussion

Before setting this property, call the [`supportsVertexAmplificationCount(_:)`](../mtldevice/supportsvertexamplificationcount%28_%29.md) method on the device object to determine whether that amplification count is supported.

## See Also

### Related Documentation
- [func setVertexAmplificationCount(Int, viewMappings: UnsafePointer<MTLVertexAmplificationViewMapping>?)](../mtlrendercommandencoder/setvertexamplificationcount%28_,viewmappings%29.md)
  Configures the number of output vertices the render pipeline produces for each input vertex, optionally with render target and viewport offsets.
- [func supportsVertexAmplificationCount(Int) -> Bool](../mtldevice/supportsvertexamplificationcount%28_%29.md)
  Returns a Boolean value that indicates whether the GPU supports an amplification factor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/maxvertexamplificationcount)*