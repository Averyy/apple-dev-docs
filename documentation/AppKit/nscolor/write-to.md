# write(to:)

**Framework**: AppKit  
**Kind**: method

Writes the color object’s data to the specified pasteboard.

**Availability**:
- macOS ?+

## Declaration

```swift
func write(to pasteBoard: NSPasteboard)
```

## Parameters

- `pasteBoard`: The pasteboard to which to write the receiver’s color data. If this pasteboard doesn’t support color data, the method does nothing.

## See Also

- [init?(from: NSPasteboard)](nscolor/init(from:).md)
  Creates a color object from color data currently on the pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/write(to:))*