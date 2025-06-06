# dialogSeverity(_:)

**Framework**: SwiftUI  
**Kind**: method

**Availability**:
- macOS 13.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func dialogSeverity(_ severity: DialogSeverity) -> some View
```

## Parameters

- `severity`: The severity to use for confirmation dialogs   and alerts.

## See Also

- [func dialogIcon(Image?) -> some View](view/dialogicon(_:).md)
  Configures the icon used by dialogs within this view.
- [func dialogIcon(Image?) -> some Scene](scene/dialogicon(_:).md)
  Configures the icon used by alerts.
- [func dialogSeverity(DialogSeverity) -> some Scene](scene/dialogseverity(_:).md)
  Sets the severity for alerts.
- [func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some View](view/dialogsuppressiontoggle(issuppressed:).md)
  Enables user suppression of dialogs and alerts presented within `self`, with a default suppression message on macOS. Unused on other platforms.
- [func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some Scene](scene/dialogsuppressiontoggle(issuppressed:).md)
  Enables user suppression of an alert with a custom suppression message.
- [func dialogSuppressionToggle(_:isSuppressed:)](view/dialogsuppressiontoggle(_:issuppressed:).md)
  Enables user suppression of dialogs and alerts presented within `self`, with a custom suppression message on macOS. Unused on other platforms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/dialogseverity(_:))*