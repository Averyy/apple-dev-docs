# subscript(_:)

**Framework**: RealityKit  
**Kind**: subscript

Gets or sets the component of the specified type.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@abi(@MainActor @preconcurrency subscript<T>(optimized componentType: T.Type) -> T? where T : Component { get set }) @MainActor @preconcurrency subscript<T>(componentType: T.Type) -> T? where T : Component { get set }
```

## See Also

- [subscript(any Component.Type) -> (any Component)?](entity/componentset/subscript(_:)-47rhg.md)
  Gets or sets the component with a specific dynamically supplied type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/componentset/subscript(_:)-5wdsf)*