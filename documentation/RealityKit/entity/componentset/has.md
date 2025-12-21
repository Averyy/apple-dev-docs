# has(_:)

**Framework**: RealityKit  
**Kind**: method

Returns a Boolean value that indicates whether the set contains a component of the given type.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func has(_ componentType: any Component.Type) -> Bool
```

#### Return Value

A Boolean value that’s `true` if the set contains a component of the given type.

## Parameters

- `componentType`: A component type, like  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/componentset/has(_:))*