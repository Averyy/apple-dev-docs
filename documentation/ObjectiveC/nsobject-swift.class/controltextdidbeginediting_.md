# controlTextDidBeginEditing:

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Sent when a control with editable text begins an editing session.

**Availability**:
- macOS 10.0+ - Deprecated in 11.0

## Declaration

```objc
- (void) controlTextDidBeginEditing:(NSNotification *) obj;
```

#### Discussion

This method is invoked when the user begins editing text in a control such as a text field or a form field. The control posts a [`textDidBeginEditingNotification`](../../AppKit/nscontrol/textdidbegineditingnotification.md) notification, and if the control’s delegate implements this method, it is automatically registered to receive the notification. Use the key `@"NSFieldEditor"` to obtain the field editor from the `userInfo` dictionary of the notification object.

See [`controlTextDidEndEditing:`](./controltextdidendediting_.md) for an explanation of why you may not always get one invocation of [`controlTextDidBeginEditing:`](./controltextdidbeginediting_.md) for each invocation of [`controlTextDidEndEditing:`](./controltextdidendediting_.md).

## Parameters

- `obj`: The notification object. The name of the notification is always [`textDidBeginEditingNotification`](../../AppKit/nscontrol/textdidbegineditingnotification.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/controltextdidbeginediting:)*