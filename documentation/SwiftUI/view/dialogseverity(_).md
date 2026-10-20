# dialogSeverity(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 13.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func dialogSeverity(_ severity: DialogSeverity) -> some View
```

## Parameters

- `severity`: The severity to use for confirmation dialogs and alerts.

## See Also

### Configuring a dialog
- [func dialogIcon(Image?) -> some View](./dialogicon%28_%29.md)
  Configures the icon used by dialogs within this view.
- [func dialogIcon(Image?) -> some Scene](../scene/dialogicon%28_%29.md)
  Configures the icon used by alerts.
- [func dialogSeverity(DialogSeverity) -> some Scene](../scene/dialogseverity%28_%29.md)
  Sets the severity for alerts.
- [func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some View](./dialogsuppressiontoggle%28issuppressed%29.md)
  Enables user suppression of dialogs and alerts presented within `self`, with a default suppression message on macOS. Unused on other platforms.
- [func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some Scene](../scene/dialogsuppressiontoggle%28issuppressed%29.md)
  Enables user suppression of an alert with a custom suppression message.
- [func dialogSuppressionToggle(_:isSuppressed:)](./dialogsuppressiontoggle%28_,issuppressed%29.md)
  Enables user suppression of dialogs and alerts presented within `self`, with a custom suppression message on macOS. Unused on other platforms.
- [func dialogSuppressionToggle(_:isSuppressed:)](../scene/dialogsuppressiontoggle%28_,issuppressed%29.md)
  Enables user suppression of an alert with a custom suppression message.
- [func dialogPreventsAppTermination(Bool?) -> some View](./dialogpreventsapptermination%28_%29.md)
  Whether the alert or confirmation dialog prevents the app from being quit/terminated by the system or app termination menu item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/dialogseverity(_:))*