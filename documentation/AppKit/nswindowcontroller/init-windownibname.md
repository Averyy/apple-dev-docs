# init(windowNibName:)

**Framework**: AppKit  
**Kind**: init

Returns a window controller initialized with a nib file.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
convenience init(windowNibName: NSNib.Name)
```

#### Discussion

Sets the owner of the nib file to the receiver. The default initialization turns on cascading, sets the [`shouldCloseDocument`](nswindowcontroller/shouldclosedocument.md) property to [`false`](https://developer.apple.com/documentation/swift/false), and sets the autosave name for the window’s frame to an empty string.

## Parameters

- `windowNibName`: The name of the nib file (minus the “ ” extension) that archives the receiver’s window; cannot be  .

## See Also

- [init(window: NSWindow?)](nswindowcontroller/init(window:).md)
  Returns a window controller initialized with a given window.
- [convenience init(windowNibName: NSNib.Name, owner: Any)](nswindowcontroller/init(windownibname:owner:).md)
  Returns a window controller initialized with a nib file and a specified owner for that nib file.
- [convenience init(windowNibPath: String, owner: Any)](nswindowcontroller/init(windownibpath:owner:).md)
  Returns a window controller initialized with a nib file at an absolute path and a specified owner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowcontroller/init(windownibname:))*