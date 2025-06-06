# controlTextDidBeginEditing(_:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the control started editing its text content.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func controlTextDidBeginEditing(_ obj: Notification)
```

#### Discussion

Use the key `“NSFieldEditor”` to obtain the field editor from the notification object’s `userInfo` dictionary.

## Parameters

- `obj`: A notification object that contains details about the editing configuration.

## See Also

- [func controlTextDidChange(Notification)](nscontroltexteditingdelegate/controltextdidchange(_:).md)
  Tells the delegate that the control made changes to its text content.
- [func controlTextDidEndEditing(Notification)](nscontroltexteditingdelegate/controltextdidendediting(_:).md)
  Tells the delegate that the control finished editing its text content and committed the changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontroltexteditingdelegate/controltextdidbeginediting(_:))*