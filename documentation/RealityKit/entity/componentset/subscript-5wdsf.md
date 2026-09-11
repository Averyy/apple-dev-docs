# subscript(_:)

**Framework**: RealityKit  
**Kind**: subscript

Gets or sets the component of the specified type.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@abi(@MainActor @preconcurrency subscript<T>(optimized componentType: T.Type) -> T? where T : Component { get set }) @MainActor @preconcurrency subscript<T>(componentType: T.Type) -> T? where T : Component { get set }
```

## See Also

- [subscript(any Component.Type) -> (any Component)?](entity/componentset/subscript(_:)-47rhg.md)
  Gets or sets the component with a specific dynamically supplied type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/componentset/subscript(_:)-5wdsf)*