# subscript(_:)

**Framework**: RealityKit  
**Kind**: subscript  
**Role**: Instance Subscript

Gets or sets the component with a specific dynamically supplied type.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency subscript(componentType: any Component.Type) -> (any Component)? { get set }
```

**Other overloads**:

```swift
@abi(@MainActor @preconcurrency subscript<T>(optimized componentType: T.Type) -> T? where T : Component { get set }) @MainActor @preconcurrency subscript<T>(componentType: T.Type) -> T? where T : Component { get set }
```

```swift
@abi(@MainActor @preconcurrency subscript<T>(optimized componentType: T.Type) -> T? where T : _ImplicitlyAnimatableBuiltinComponent { get set }) @MainActor @preconcurrency subscript<T>(componentType: T.Type) -> T? where T : _ImplicitlyAnimatableBuiltinComponent { get set }
```

## See Also

### Accessing members
- [subscript<T>(T.Type) -> T?](./subscript%28_%29-5wdsf.md)
  Gets or sets the component of the specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/componentset/subscript(_:)-47rhg)*