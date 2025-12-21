# fragmentStaticLinkingDescriptor

**Framework**: Metal  
**Kind**: property

Provides static linking information for the fragment stage of the render pipeline.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@NSCopying
var fragmentStaticLinkingDescriptor: MTL4StaticLinkingDescriptor! { get set }
```

#### Discussion

Use this property to link extra shader functions to the fragment stage of the render pipeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4meshrenderpipelinedescriptor/fragmentstaticlinkingdescriptor)*