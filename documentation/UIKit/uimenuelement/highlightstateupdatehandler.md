# highlightStateUpdateHandler

**Framework**: UIKit  
**Kind**: property

A closure the system calls when the element’s highlight state changes in a menu.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var highlightStateUpdateHandler: ((UIMenuElement, Bool) -> Void)? { get set }
```

#### Discussion

The system calls this handler whenever a menu element transitions between highlighted and unhighlighted states. Highlight events include pointer hover, touch down, keyboard navigation, and focus changes.

The handler receives two parameters: the affected element and a Boolean that indicates the new state. When `isHighlighted` is [`true`](https://developer.apple.com/documentation/Swift/true), the element is highlighted. When it’s [`false`](https://developer.apple.com/documentation/Swift/false), the element is unhighlighted.

Use this handler to update your app’s UI in response to the user’s attention on a menu element, such as showing a preview of the action’s effect while the user considers the option.

> **Note**: In visionOS, the system doesn’t call this handler for gaze-based highlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenuelement/highlightstateupdatehandler)*