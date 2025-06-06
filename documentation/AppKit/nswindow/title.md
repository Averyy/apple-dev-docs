# title

**Framework**: AppKit  
**Kind**: property

The string that appears in the title bar of the window or the path to the represented file.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var title: String { get set }
```

#### Discussion

If the title has been set using [`setTitleWithRepresentedFilename(_:)`](nswindow/settitlewithrepresentedfilename(_:).md), this property contains the file’s path. Setting this property also sets the title of the window’s miniaturized window.

## See Also

- [var miniwindowTitle: String!](nswindow/miniwindowtitle.md)
  The title displayed in the window’s minimized window.
- [var subtitle: String](nswindow/subtitle.md)
  A secondary line of text that appears in the title bar of the window.
- [var titleVisibility: NSWindow.TitleVisibility](nswindow/titlevisibility-swift.property.md)
  A value that indicates the visibility of the window’s title and title bar buttons.
- [func setTitleWithRepresentedFilename(String)](nswindow/settitlewithrepresentedfilename(_:).md)
  Sets a given path as the window’s title, formatting it as a file-system path, and records this path as the window’s associated file.
- [var representedFilename: String](nswindow/representedfilename.md)
  The path to the file of the window’s represented file.
- [var representedURL: URL?](nswindow/representedurl.md)
  The URL of the file the window represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/title)*