# ultraDark

**Framework**: SwiftUI  
**Kind**: property

An effect that dims passthrough video more than [`dark`](surroundingseffect/dark.md)

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
static var ultraDark: SurroundingsEffect { get }
```

#### Discussion

Use this value with the [`preferredSurroundingsEffect(_:)`](view/preferredsurroundingseffect(_:).md) view modifier when you want to dim passthrough video while displaying a particular view. Doing so helps to draw attention to your app’s content while still enabling people to remain aware of their surroundings. This effect will only be applied while an immersive space is opened.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/surroundingseffect/ultradark)*