# AccessibilityQuickActionStyle

**Framework**: SwiftUI  
**Kind**: protocol

A type that describes the presentation style of an accessibility quick action.

**Availability**:
- watchOS 9.0+

## Declaration

```swift
protocol AccessibilityQuickActionStyle
```

## Topics

### Getting built-in menu styles
- [static var outline: AccessibilityQuickActionOutlineStyle](accessibilityquickactionstyle/outline.md)
  A presentation style that animates an outline around the view when the accessibility quick action is active.
- [static var prompt: AccessibilityQuickActionPromptStyle](accessibilityquickactionstyle/prompt.md)
  A presentation style that displays a prompt to the user when the accessibility quick action is active.
### Supporting types
- [struct AccessibilityQuickActionOutlineStyle](accessibilityquickactionoutlinestyle.md)
  A presentation style that displays a prompt to the user when the accessibility quick action is active.
- [struct AccessibilityQuickActionPromptStyle](accessibilityquickactionpromptstyle.md)
  A presentation style that displays a prompt to the user when the accessibility quick action is active.

## Relationships

### Conforming Types
- [AccessibilityQuickActionOutlineStyle](accessibilityquickactionoutlinestyle.md)
- [AccessibilityQuickActionPromptStyle](accessibilityquickactionpromptstyle.md)

## See Also

- [func accessibilityQuickAction<Style, Content>(style: Style, content: () -> Content) -> some View](view/accessibilityquickaction(style:content:).md)
  Adds a quick action to be shown by the system when active.
- [func accessibilityQuickAction<Style, Content>(style: Style, isActive: Binding<Bool>, content: () -> Content) -> some View](view/accessibilityquickaction(style:isactive:content:).md)
  Adds a quick action to be shown by the system when active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessibilityquickactionstyle)*