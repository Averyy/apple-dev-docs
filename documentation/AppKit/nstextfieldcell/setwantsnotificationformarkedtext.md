# setWantsNotificationForMarkedText(_:)

**Framework**: AppKit  
**Kind**: method

Directs the cell’s associated field editor to post text change notifications.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func setWantsNotificationForMarkedText(_ flag: Bool)
```

## Parameters

- `flag`: If  , the field editor posts text change notifications (NSTextDidChangeNotification) while editing marked text; if  , notifications are delayed until the marked text confirmation.

## See Also

- [func setUpFieldEditorAttributes(NSText) -> NSText](nstextfieldcell/setupfieldeditorattributes(_:).md)
  Allows the cell to set up the field editor’s attributes before editing begins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfieldcell/setwantsnotificationformarkedtext(_:))*