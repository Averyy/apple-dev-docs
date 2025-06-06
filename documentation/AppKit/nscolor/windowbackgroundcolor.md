# windowBackgroundColor

**Framework**: AppKit  
**Kind**: property

The color to use for the window background.

**Availability**:
- macOS ?+

## Declaration

```swift
class var windowBackgroundColor: NSColor { get }
```

#### Return Value

The window background color.

#### Discussion

When applied to an [`NSBox`](nsbox.md) object, this color supports Desktop Tinting in Dark Mode. With Desktop Tinting, the system modifies this color dynamically by incorporating some of the color from the underlying desktop image. The system does not apply this dynamic tinting effect to other types of views.

## See Also

- [class var windowFrameTextColor: NSColor](nscolor/windowframetextcolor.md)
  The color to use for text in a window’s frame.
- [class var underPageBackgroundColor: NSColor](nscolor/underpagebackgroundcolor.md)
  The color to use in the area beneath your window’s views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/windowbackgroundcolor)*