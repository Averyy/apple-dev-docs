# subscript(withoutAnimation:)

**Framework**: RealityKit  
**Kind**: subscript

Gets or sets the component of the specified type, without considering implicit animations.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency subscript<T>(withoutAnimation componentType: T.Type) -> T? where T : Component { get set }
```

#### Overview

This is only useful in specialized circumstances, such as in a tight loop, where you are certain there are no animations active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/subscript(withoutanimation:))*