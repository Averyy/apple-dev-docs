# init(windowNibPath:owner:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Returns a window controller initialized with a nib file at an absolute path and a specified owner.

**Availability**:
- macOS

## Declaration

```swift
convenience init(windowNibPath: String, owner: Any)
```

```objc
- (instancetype) initWithWindowNibPath:(NSString *) windowNibPath owner:(id) owner;
```

## Discussion

Use this method if your nib file is at a fixed location (which is not inside either the file’s owner’s class’s bundle or in the application’s main bundle). The default initialization turns on cascading, sets the [`shouldCloseDocument`](./shouldclosedocument.md) property to [`false`](../../Swift/false.md), and sets the autosave name for the window’s frame to an empty string.

## Parameters

- `windowNibPath`: The full path to the nib file that archives the receiver’s window; cannot be `nil`.
- `owner`: The nib file’s owner; cannot be `nil`.

## See Also

### Initializing Window Controllers
- [init(window: NSWindow?)](./init%28window%29.md)
  Returns a window controller initialized with a given window.
- [convenience init(windowNibName: NSNib.Name)](./init%28windownibname%29.md)
  Returns a window controller initialized with a nib file.
- [convenience init(windowNibName: NSNib.Name, owner: Any)](./init%28windownibname,owner%29.md)
  Returns a window controller initialized with a nib file and a specified owner for that nib file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowcontroller/init(windownibpath:owner:))*