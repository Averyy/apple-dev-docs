# init(windowNibPath:owner:)

**Framework**: AppKit  
**Kind**: init

Returns a window controller initialized with a nib file at an absolute path and a specified owner.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
convenience init(windowNibPath: String, owner: Any)
```

#### Discussion

Use this method if your nib file is at a fixed location (which is not inside either the file’s owner’s class’s bundle or in the application’s main bundle). The default initialization turns on cascading, sets the [`shouldCloseDocument`](nswindowcontroller/shouldclosedocument.md) property to [`false`](https://developer.apple.com/documentation/swift/false), and sets the autosave name for the window’s frame to an empty string.

## Parameters

- `windowNibPath`: The full path to the nib file that archives the receiver’s window; cannot be  .
- `owner`: The nib file’s owner; cannot be  .

## See Also

- [init(window: NSWindow?)](nswindowcontroller/init(window:).md)
  Returns a window controller initialized with a given window.
- [convenience init(windowNibName: NSNib.Name)](nswindowcontroller/init(windownibname:).md)
  Returns a window controller initialized with a nib file.
- [convenience init(windowNibName: NSNib.Name, owner: Any)](nswindowcontroller/init(windownibname:owner:).md)
  Returns a window controller initialized with a nib file and a specified owner for that nib file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowcontroller/init(windownibpath:owner:))*