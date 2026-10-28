# set(_:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

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
@preconcurrency func set<T>(_ component: T) where T : _ImplicitlyAnimatableBuiltinComponent
```

**Other overloads**:

```swift
@MainActor
@preconcurrency func set(_ components: [any Component])
```

```swift
@MainActor
@preconcurrency func set<T>(_ component: T) where T : Component
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/componentset/set(_:)-ogkv)*