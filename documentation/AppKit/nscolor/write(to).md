# write(to:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Writes the color object’s data to the specified pasteboard.

**Availability**:
- macOS

## Declaration

```swift
func write(to pasteBoard: NSPasteboard)
```

```objc
- (void) writeToPasteboard:(NSPasteboard *) pasteBoard;
```

## Parameters

- `pasteBoard`: The pasteboard to which to write the receiver’s color data. If this pasteboard doesn’t support color data, the method does nothing.

## See Also

### Copying and pasting color Information
- [init?(from: NSPasteboard)](./init%28from%29.md)
  Creates a color object from color data currently on the pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/write(to:))*