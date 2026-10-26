# controlTextDidChange:

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Sent when the text in the receiving control changes.

**Availability**:
- macOS 10.0+ - Deprecated in 11.0

## Declaration

```objc
- (void) controlTextDidChange:(NSNotification *) obj;
```

#### Discussion

This method is invoked when text in a control such as a text field or form changes. The control posts a [`textDidChangeNotification`](../../AppKit/nscontrol/textdidchangenotification.md) notification, and if the control’s delegate implements this method, it is automatically registered to receive the notification. Use the key `@"NSFieldEditor"` to obtain the field editor from the `userInfo` dictionary of the notification object.

## Parameters

- `obj`: The notification object. The name of the notification is always [`textDidChangeNotification`](../../AppKit/nscontrol/textdidchangenotification.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/controltextdidchange:)*