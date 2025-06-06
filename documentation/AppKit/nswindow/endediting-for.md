# endEditing(for:)

**Framework**: AppKit  
**Kind**: method

Forces the field editor to give up its first responder status and prepares it for its next assignment.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func endEditing(for object: Any?)
```

#### Discussion

If the field editor is the first responder, it’s made to resign that status even if its [`resignFirstResponder()`](nsresponder/resignfirstresponder().md) method returns [`false`](https://developer.apple.com/documentation/swift/false). This registration forces the field editor to send a [`textDidEndEditing(_:)`](nstextdelegate/textdidendediting(_:).md) message to its delegate. The field editor is then removed from the view hierarchy, its delegate is set to `nil`, and it’s emptied of any text it may contain.

This method is typically invoked by the object using the field editor when it’s finished. Other objects normally change the first responder by simply using [`makeFirstResponder(_:)`](nswindow/makefirstresponder(_:).md), which allows a field editor or other object to retain its first responder status if, for example, the user has entered an invalid value. The [`endEditing(for:)`](nswindow/endediting(for:).md) method should be used only as a last resort if the field editor refuses to resign first responder status. Even in this case, you should always allow the field editor a chance to validate its text and take whatever other action it needs first. You can do this by first trying to make the `NSWindow` object the first responder:

```objc
if ([myWindow makeFirstResponder:myWindow]) {
    /* All fields are now valid; it’s safe to use fieldEditor:forObject:
        to claim the field editor. */
}
else {
    /* Force first responder to resign. */
    [myWindow endEditingFor:nil];
}
```

## Parameters

- `object`: The object that is using the window’s field editor.

## See Also

- [func windowWillReturnFieldEditor(NSWindow, to: Any?) -> Any?](nswindowdelegate/windowwillreturnfieldeditor(_:to:).md)
  Tells the delegate that the field editor for a text-displaying object has been requested.
- [func fieldEditor(Bool, for: Any?) -> NSText?](nswindow/fieldeditor(_:for:).md)
  Returns the window’s field editor, creating it if requested.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/endediting(for:))*