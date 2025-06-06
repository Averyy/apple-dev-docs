# windowWillReturnFieldEditor(_:to:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the field editor for a text-displaying object has been requested.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func windowWillReturnFieldEditor(_ sender: NSWindow, to client: Any?) -> Any?
```

#### Return Value

The field editor for `client`; returns `nil` when the delegate has no field editor to assign.

## Parameters

- `sender`: The window requesting the field editor from the delegate.
- `client`: A text-displaying object to be associated with the field editor. If  , the requested field editor is the default.

## See Also

- [func fieldEditor(Bool, for: Any?) -> NSText?](nswindow/fieldeditor(_:for:).md)
  Returns the window’s field editor, creating it if requested.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowwillreturnfieldeditor(_:to:))*