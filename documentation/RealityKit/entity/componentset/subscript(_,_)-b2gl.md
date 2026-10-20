# subscript(_:_:)

**Framework**: RealityKit  
**Kind**: subscript  
**Role**: Instance Subscript

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency subscript<T>(componentType: T.Type, backDeploy: Void = ()) -> T? where T : _ImplicitlyAnimatableBuiltinComponent { get set }
```

**Other overloads**:

```swift
@MainActor
@preconcurrency subscript<T>(componentType: T.Type, backDeploy: Void = ()) -> T? where T : Component { get set }
```

## See Also

### Accessing animatable components
- [subscript<T>(componentType _: T.Type) -> T?](./subscript%28componenttype%29-3miek.md)
- [subscript<T>(withoutAnimation _: T.Type) -> T?](./subscript%28withoutanimation%29.md)
  Gets or sets the component of the specified type, without considering implicit animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/componentset/subscript(_:_:)-b2gl)*