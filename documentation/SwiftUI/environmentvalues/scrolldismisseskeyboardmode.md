# scrollDismissesKeyboardMode

**Framework**: SwiftUI  
**Kind**: property

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

The default value is [`automatic`](scrolldismisseskeyboardmode/automatic.md). Use the [`scrollDismissesKeyboard(_:)`](view/scrolldismisseskeyboard(_:).md) modifier to configure this property.

## See Also

- [func scrollDismissesKeyboard(ScrollDismissesKeyboardMode) -> some View](view/scrolldismisseskeyboard(_:).md)
  Configures the behavior in which scrollable content interacts with the software keyboard.
- [struct ScrollDismissesKeyboardMode](scrolldismisseskeyboardmode.md)
  The ways that scrollable content can interact with the software keyboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/scrolldismisseskeyboardmode)*