# allowsTypeSelect

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the context menu supports keystroke-based navigation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var allowsTypeSelect: Bool { get set }
```

#### Discussion

TypeSelect lets users move focus to a matching menu option by typing on a hardware keyboard while the menu is open. When a context menu appears alongside a text field that actively receives keyboard input, TypeSelect can intercept keystrokes before they reach the text field.

Set this property to [`false`](https://developer.apple.com/documentation/Swift/false) when the menu serves as a companion to an active text input, such as a suggestion menu or autocomplete picker. This allows keyboard input to flow to the text field without being captured by the menu’s navigation.

The default value is [`true`](https://developer.apple.com/documentation/Swift/true).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontextmenuconfiguration/allowstypeselect)*