# followsUndockedKeyboard

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines if the layout guide tracks the keyboard when it’s undocked from the bottom of the screen.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var followsUndockedKeyboard: Bool { get set }
```

#### Discussion

The default value is [`false`](https://developer.apple.com/documentation/swift/false); the guide tracks the keyboard only when docked. When the keyboard is off screen or undocked, the guide’s [`topAnchor`](uilayoutguide/topanchor.md) matches the [`bottomAnchor`](uilayoutguide/bottomanchor.md) of [`safeAreaLayoutGuide`](uiview/safearealayoutguide.md). To follow all keyboard anchors even when undocked or floating, set [`followsUndockedKeyboard`](uikeyboardlayoutguide/followsundockedkeyboard.md) to [`true`](https://developer.apple.com/documentation/swift/true).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uikeyboardlayoutguide/followsundockedkeyboard)*