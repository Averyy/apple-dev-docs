# underPageBackgroundColor

**Framework**: AppKit  
**Kind**: property

The color to use in the area beneath your window’s views.

**Availability**:
- macOS 10.8+

## Declaration

```swift
class var underPageBackgroundColor: NSColor { get }
```

#### Return Value

Use this color to fill the backdrop underneath your app’s main content.

#### Discussion

When applied to an [`NSBox`](nsbox.md) object, this color supports Desktop Tinting in Dark Mode. With Desktop Tinting, the system modifies this color dynamically by incorporating some of the color from the underlying desktop image. The system does not apply this dynamic tinting effect to other types of views.

## See Also

- [class var windowBackgroundColor: NSColor](nscolor/windowbackgroundcolor.md)
  The color to use for the window background.
- [class var windowFrameTextColor: NSColor](nscolor/windowframetextcolor.md)
  The color to use for text in a window’s frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/underpagebackgroundcolor)*