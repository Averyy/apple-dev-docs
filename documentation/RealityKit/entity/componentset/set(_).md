# set(_:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Adds multiple components to the set, overriding any existing components of the same type.

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
@preconcurrency func set(_ components: [any Component])
```

**Other overloads**:

```swift
@MainActor
@preconcurrency func set<T>(_ component: T) where T : Component
```

```swift
@MainActor
@preconcurrency func set<T>(_ component: T) where T : _ImplicitlyAnimatableBuiltinComponent
```

#### Discussion

If the input array includes multiple components of the same type, the set adds the component with the highest index. This is because the set can only hold one component of each type.

## Parameters

- `components`: An array of components to add.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/componentset/set(_:))*