# vertexStaticLinkingDescriptor

**Framework**: Metal  
**Kind**: property

Provides static linking information for the vertex stage of the render pipeline.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@NSCopying
var vertexStaticLinkingDescriptor: MTL4StaticLinkingDescriptor! { get set }
```

#### Discussion

Use this property to link extra shader functions to the vertex stage of the render pipeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4renderpipelinedescriptor/vertexstaticlinkingdescriptor)*