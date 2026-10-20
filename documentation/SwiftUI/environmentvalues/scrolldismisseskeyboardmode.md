# scrollDismissesKeyboardMode

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The way that scrollable content interacts with the software keyboard.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
var scrollDismissesKeyboardMode: ScrollDismissesKeyboardMode { get set }
```

#### Discussion

The default value is [`automatic`](../scrolldismisseskeyboardmode/automatic.md). Use the [`scrollDismissesKeyboard(_:)`](../view/scrolldismisseskeyboard%28_%29.md) modifier to configure this property.

## See Also

### Interacting with a software keyboard
- [func scrollDismissesKeyboard(ScrollDismissesKeyboardMode) -> some View](../view/scrolldismisseskeyboard%28_%29.md)
  Configures the behavior in which scrollable content interacts with the software keyboard.
- [struct ScrollDismissesKeyboardMode](../scrolldismisseskeyboardmode.md)
  The ways that scrollable content can interact with the software keyboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/scrolldismisseskeyboardmode)*