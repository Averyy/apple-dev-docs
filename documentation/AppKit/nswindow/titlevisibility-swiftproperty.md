# titleVisibility

**Framework**: AppKit  
**Kind**: property

A value that indicates the visibility of the window’s title and title bar buttons.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var titleVisibility: NSWindow.TitleVisibility { get set }
```

#### Discussion

By default, the value of this property is [`NSWindow.TitleVisibility.visible`](nswindow/titlevisibility-swift.enum/visible.md).

## See Also

- [var title: String](nswindow/title.md)
  The string that appears in the title bar of the window or the path to the represented file.
- [var subtitle: String](nswindow/subtitle.md)
  A secondary line of text that appears in the title bar of the window.
- [func setTitleWithRepresentedFilename(String)](nswindow/settitlewithrepresentedfilename(_:).md)
  Sets a given path as the window’s title, formatting it as a file-system path, and records this path as the window’s associated file.
- [var representedFilename: String](nswindow/representedfilename.md)
  The path to the file of the window’s represented file.
- [var representedURL: URL?](nswindow/representedurl.md)
  The URL of the file the window represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/titlevisibility-swift.property)*