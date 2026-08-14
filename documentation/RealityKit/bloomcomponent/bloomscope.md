# BloomComponent.BloomScope

**Framework**: RealityKit  
**Kind**: struct

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct BloomScope
```

## Topics

### Accessing bloom scopes
- [static let hierarchical: BloomComponent.BloomScope](bloomcomponent/bloomscope/hierarchical.md)
  Bloom is restricted to the bounding box of the attached entity’s mesh hierarchy.
- [static let unbounded: BloomComponent.BloomScope](bloomcomponent/bloomscope/unbounded.md)
  Bloom is computed on the entire screen with no bounding box restriction.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var scope: BloomComponent.BloomScope](bloomcomponent/scope.md)
  The scope of where bloom will be computed


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/bloomcomponent/bloomscope)*