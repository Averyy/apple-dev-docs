# setWantsNotificationForMarkedText(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Directs the cell’s associated field editor to post text change notifications.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func setWantsNotificationForMarkedText(_ flag: Bool)
```

```objc
- (void) setWantsNotificationForMarkedText:(BOOL) flag;
```

## Parameters

- `flag`: If [`true`](../../Swift/true.md), the field editor posts text change notifications (NSTextDidChangeNotification) while editing marked text; if [`false`](../../Swift/false.md), notifications are delayed until the marked text confirmation.

## See Also

### Managing the Field Editor
- [func setUpFieldEditorAttributes(NSText) -> NSText](./setupfieldeditorattributes%28_%29.md)
  Allows the cell to set up the field editor’s attributes before editing begins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfieldcell/setwantsnotificationformarkedtext(_:))*