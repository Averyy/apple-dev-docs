# textRenderer(_:)

**Framework**: FamilyControls  
**Kind**: method

Returns a new view such that any text views within it will use `renderer` to draw themselves.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
func textRenderer<T>(_ renderer: T) -> some View where T : TextRenderer
```

#### Return Value

A new view that will use `renderer` to draw its text views.

## Parameters

- `renderer`: The renderer value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivityiconview/textrenderer(_:))*