# formStyle(_:)

**Framework**: RealityKit  
**Kind**: method

Sets the style for forms in a view hierarchy.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func formStyle<S>(_ style: S) -> some View where S : FormStyle
```

#### Return Value

A view that uses the specified form style for itself and its child views.

## Parameters

- `style`: The form style to set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/resolvedmodel3d/formstyle(_:))*