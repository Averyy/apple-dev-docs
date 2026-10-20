# BloomComponent.BloomScope

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct BloomScope
```

## Topics

### Accessing bloom scopes
- [static let hierarchical: BloomComponent.BloomScope](./bloomscope/hierarchical.md)
  Bloom is restricted to the bounding box of the attached entity’s mesh hierarchy.
- [static let unbounded: BloomComponent.BloomScope](./bloomscope/unbounded.md)
  Bloom is computed on the entire screen with no bounding box restriction.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the bloom scope
- [var scope: BloomComponent.BloomScope](./scope.md)
  The scope of where bloom will be computed


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/bloomcomponent/bloomscope)*