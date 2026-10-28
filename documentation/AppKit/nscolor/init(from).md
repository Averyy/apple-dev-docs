# init(from:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a color object from color data currently on the pasteboard.

**Availability**:
- macOS

## Declaration

```swift
init?(from pasteBoard: NSPasteboard)
```

```objc
+ (NSColor *) colorFromPasteboard:(NSPasteboard *) pasteBoard;
```

## Return Value

The color currently on the pasteboard or `nil` if `pasteBoard` doesn’t contain color data. The returned color’s alpha component is set to 1.0 if [`ignoresAlpha`](./ignoresalpha.md) returns [`true`](../../Swift/true.md).

## Parameters

- `pasteBoard`: The pasteboard from which to return the color.

## See Also

### Copying and pasting color Information
- [func write(to: NSPasteboard)](./write%28to%29.md)
  Writes the color object’s data to the specified pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/init(from:))*