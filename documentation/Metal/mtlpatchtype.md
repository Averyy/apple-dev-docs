# MTLPatchType

**Framework**: Metal  
**Kind**: enum

Types of tessellation patches that can be inputs of a post-tessellation vertex function.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
enum MTLPatchType
```

## Topics

### Patch types
- [MTLPatchType.none](mtlpatchtype/none.md)
  An option that indicates that this isn’t a post-tessellation vertex function.
- [MTLPatchType.triangle](mtlpatchtype/triangle.md)
  A triangle patch.
- [MTLPatchType.quad](mtlpatchtype/quad.md)
  A quad patch.
### Initializers
- [init?(rawValue: UInt)](mtlpatchtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var patchType: MTLPatchType](mtlfunction/patchtype.md)
  The tessellation patch type of a post-tessellation vertex function.
- [var patchControlPointCount: Int](mtlfunction/patchcontrolpointcount.md)
  The number of patch control points in the post-tessellation vertex function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpatchtype)*