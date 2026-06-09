# subscript(componentType:)

**Framework**: RealityKit  
**Kind**: subscript

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@abi(@MainActor @preconcurrency subscript<T>(componentType: T.Type) -> T? where T : _ImplicitlyAnimatableBuiltinComponent { get set }) @MainActor @preconcurrency subscript<T>(componentType componentType: T.Type) -> T? where T : _ImplicitlyAnimatableBuiltinComponent { get set }
```

## See Also

- [subscript<T>(T.Type, Void) -> T?](entity/componentset/subscript(_:_:)-b2gl.md)
- [subscript<T>(withoutAnimation _: T.Type) -> T?](entity/componentset/subscript(withoutanimation:).md)
  Gets or sets the component of the specified type, without considering implicit animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/componentset/subscript(componenttype:)-3miek)*