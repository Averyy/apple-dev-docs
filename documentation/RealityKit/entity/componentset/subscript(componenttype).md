# subscript(componentType:)

**Framework**: RealityKit  
**Kind**: subscript  
**Role**: Instance Subscript

Gets or sets the component of the specified type.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@abi(@MainActor @preconcurrency subscript<T>(componentType: T.Type) -> T? where T : Component { get set }) @MainActor @preconcurrency subscript<T>(componentType componentType: T.Type) -> T? where T : Component { get set }
```

**Other overloads**:

```swift
@abi(@MainActor @preconcurrency subscript<T>(componentType: T.Type) -> T? where T : _ImplicitlyAnimatableBuiltinComponent { get set }) @MainActor @preconcurrency subscript<T>(componentType componentType: T.Type) -> T? where T : _ImplicitlyAnimatableBuiltinComponent { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/componentset/subscript(componenttype:))*