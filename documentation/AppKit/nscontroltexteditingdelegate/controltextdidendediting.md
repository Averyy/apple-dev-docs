# controlTextDidEndEditing(_:)

**Framework**: Appkit  
**Kind**: method

Tells the delegate that the control finished editing its text content and committed the changes.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func controlTextDidEndEditing(_ obj: Notification)
```

#### Discussion

Use the key `“NSFieldEditor”` to obtain the field editor from the notification object’s `userInfo` dictionary.

> **Note**:  If you call [`abortEditing()`](nscontrol/abortediting().md) to discard pending edits, the control doesn’t call [`controlTextDidEndEditing(_:)`](nscontroltexteditingdelegate/controltextdidendediting(_:).md).

## Parameters

- `obj`: A notification object that contains details about the editing configuration.

## See Also

- [func controlTextDidBeginEditing(Notification)](nscontroltexteditingdelegate/controltextdidbeginediting(_:).md)
  Tells the delegate that the control started editing its text content.
- [func controlTextDidChange(Notification)](nscontroltexteditingdelegate/controltextdidchange(_:).md)
  Tells the delegate that the control made changes to its text content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontroltexteditingdelegate/controltextdidendediting(_:))*