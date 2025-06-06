# MTLPatchType.quad

**Framework**: Metal  
**Kind**: case

A quad patch.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case quad
```

#### Discussion

Metal uses this value if the shader is a post-tessellation vertex function with the `[[patch(quad)]]` attribute.

## See Also

- [MTLPatchType.none](mtlpatchtype/none.md)
  An option that indicates that this isn’t a post-tessellation vertex function.
- [MTLPatchType.triangle](mtlpatchtype/triangle.md)
  A triangle patch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpatchtype/quad)*