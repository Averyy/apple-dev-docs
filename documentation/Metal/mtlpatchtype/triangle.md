# MTLPatchType.triangle

**Framework**: Metal  
**Kind**: case  
**Role**: Case

A triangle patch.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case triangle
```

```c
MTLPatchTypeTriangle
```

#### Discussion

Metal uses this value if the shader is a post-tessellation vertex function with the `[[patch(triangle)]]` attribute.

## See Also

### Patch types
- [MTLPatchType.none](./none.md)
  An option that indicates that this isn’t a post-tessellation vertex function.
- [MTLPatchType.quad](./quad.md)
  A quad patch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpatchtype/triangle)*