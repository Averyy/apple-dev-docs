# close()

**Framework**: AppKit  
**Kind**: method

Closes the window if it was loaded.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func close()
```

#### Discussion

Because this method closes the window without asking the user for confirmation, you usually do not invoke it when the Close menu command is chosen. Instead invoke NSWindow’s [`performClose(_:)`](nswindow/performclose(_:).md) on the receiver’s window.

## See Also

- [var shouldCloseDocument: Bool](nswindowcontroller/shouldclosedocument.md)
  A Boolean value that indicates whether the receiver necessarily closes the associated document when the window it manages is closed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowcontroller/close())*