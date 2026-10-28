# controlTextDidBeginEditing(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the control started editing its text content.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func controlTextDidBeginEditing(_ obj: Notification)
```

```objc
- (void) controlTextDidBeginEditing:(NSNotification *) obj;
```

## Discussion

Use the key `“NSFieldEditor”` to obtain the field editor from the notification object’s `userInfo` dictionary.

## Parameters

- `obj`: A notification object that contains details about the editing configuration.

## See Also

### Instance Methods
- [func controlTextDidChange(Notification)](./controltextdidchange%28_%29.md)
  Tells the delegate that the control made changes to its text content.
- [func controlTextDidEndEditing(Notification)](./controltextdidendediting%28_%29.md)
  Tells the delegate that the control finished editing its text content and committed the changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontroltexteditingdelegate/controltextdidbeginediting(_:))*