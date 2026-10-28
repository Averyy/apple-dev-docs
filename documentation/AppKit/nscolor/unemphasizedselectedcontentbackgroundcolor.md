# unemphasizedSelectedContentBackgroundColor

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The color to use for selected and unemphasized content.

**Availability**:
- macOS 10.14+

## Declaration

```swift
class var unemphasizedSelectedContentBackgroundColor: NSColor { get }
```

```objc
@property (class, strong, readonly) NSColor * unemphasizedSelectedContentBackgroundColor;
```

## Discussion

Use this color when the window containing the content is not key, or when the view containing the content does not have key focus.

## See Also

### Content colors
- [class var linkColor: NSColor](./linkcolor.md)
  The color to use for links.
- [class var separatorColor: NSColor](./separatorcolor.md)
  The color to use for separators between different sections of content.
- [class var selectedContentBackgroundColor: NSColor](./selectedcontentbackgroundcolor.md)
  The color to use for the background of selected and emphasized content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/unemphasizedselectedcontentbackgroundcolor)*