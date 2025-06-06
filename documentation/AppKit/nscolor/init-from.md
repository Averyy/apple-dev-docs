# init(from:)

**Framework**: AppKit  
**Kind**: init

Creates a color object from color data currently on the pasteboard.

**Availability**:
- macOS ?+

## Declaration

```swift
init?(from pasteBoard: NSPasteboard)
```

#### Return Value

The color currently on the pasteboard or `nil` if `pasteBoard` doesn’t contain color data. The returned color’s alpha component is set to 1.0 if [`ignoresAlpha`](nscolor/ignoresalpha.md) returns [`true`](https://developer.apple.com/documentation/swift/true).

## Parameters

- `pasteBoard`: The pasteboard from which to return the color.

## See Also

- [func write(to: NSPasteboard)](nscolor/write(to:).md)
  Writes the color object’s data to the specified pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/init(from:))*