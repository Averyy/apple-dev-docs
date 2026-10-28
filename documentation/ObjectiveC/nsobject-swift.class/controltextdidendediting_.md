# controlTextDidEndEditing:

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Sent when a control with editable text ends an editing session.

**Availability**:
- macOS 10.0+ - Deprecated in 11.0

## Declaration

```objc
- (void) controlTextDidEndEditing:(NSNotification *) obj;
```

## Discussion

This method is invoked when the user stops editing text in a control such as a text field or form. The control posts a [`textDidEndEditingNotification`](../../AppKit/nscontrol/textdidendeditingnotification.md) notification, and if the control’s delegate implements this method, it is automatically registered to receive the notification. Use the key `@"NSFieldEditor"` to obtain the field editor from the `userInfo` dictionary of the notification object.

> ⚠️ **Warning**:  In some cases, such as when editing within an instance of `NSOutlineView`, this method may be invoked without a previous invocation of [`controlTextDidBeginEditing:`](./controltextdidbeginediting_.md). You will only get the `controlTextDidBeginEditing:` notification if the user actually types something, but you can get the `controlTextDidEndEditing:` notification if the user just double-clicks the field and then clicks outside the field, without typing.

## Parameters

- `obj`: The notification object. The name of the notification is always [`textDidEndEditingNotification`](../../AppKit/nscontrol/textdidendeditingnotification.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/controltextdidendediting:)*