# semiDark

**Framework**: SwiftUI  
**Kind**: property

An effect that dims passthrough video less than [`dark`](surroundingseffect/dark.md).

**Availability**:
- visionOS 2.0+

## Declaration

```swift
static var semiDark: SurroundingsEffect { get }
```

#### Discussion

Use this value with the [`preferredSurroundingsEffect(_:)`](view/preferredsurroundingseffect(_:).md) view modifier when you want to dim passthrough video while displaying a particular view. Doing so helps to draw attention to your app’s content while still enabling people to remain aware of their surroundings. This value can be used in the shared space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/surroundingseffect/semidark)*