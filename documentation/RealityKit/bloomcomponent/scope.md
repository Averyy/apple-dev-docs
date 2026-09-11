# scope

**Framework**: RealityKit  
**Kind**: property

The scope of where bloom will be computed

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var scope: BloomComponent.BloomScope
```

#### Discussion

If set to unbounded, bloom will be computed on the entire screen.

If set to hierarchical, bloom will only be computed in regions near the entity hierarchy beneath all bloom components. This is useful to reduce the cost of bloom, but can create artifacts if something bright enough to bloom is not contained within the hierarchy.

## See Also

- [BloomComponent.BloomScope](bloomcomponent/bloomscope.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/bloomcomponent/scope)*