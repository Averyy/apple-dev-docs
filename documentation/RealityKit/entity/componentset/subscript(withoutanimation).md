# subscript(withoutAnimation:)

**Framework**: RealityKit  
**Kind**: subscript

Gets or sets the component of the specified type, without considering implicit animations.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@MainActor
@preconcurrency subscript<T>(withoutAnimation withoutAnimation: T.Type) -> T? where T : Component { get set }
```

#### Overview

This is only useful in specialized circumstances, such as in a tight loop, where you are certain there are no animations active.

## See Also

- [subscript<T>(componentType _: T.Type) -> T?](entity/componentset/subscript(componenttype:)-3miek.md)
- [subscript<T>(T.Type, Void) -> T?](entity/componentset/subscript(_:_:)-b2gl.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/componentset/subscript(withoutanimation:))*