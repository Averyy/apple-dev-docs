# imagePlaygroundGenerationStyle(_:in:)

**Framework**: SwiftUI  
**Kind**: method

Sets the generation style for an image playground.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
nonisolated
func imagePlaygroundGenerationStyle(_ style: ImagePlaygroundStyle, in allowedStyles: [ImagePlaygroundStyle] = ImagePlaygroundStyle.all) -> some View
```

#### Return Value

An image playground sheet that uses one of the specified generation `styles`.

## Parameters

- `style`: The generation style that the playground uses.
- `allowedStyles`: The list of generation styles that the   input can have.   Use   to check the list of all possible styles, and pass a subset of those.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/imageplaygroundgenerationstyle(_:in:))*