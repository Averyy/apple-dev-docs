# subtitle

**Framework**: AppKit  
**Kind**: property

A secondary line of text that appears in the title bar of the window.

**Availability**:
- macOS 11.0+

## Declaration

```swift
@MainActor
var subtitle: String { get set }
```

#### Discussion

When this property is an empty string, the system removes the subtitle from the window layout.

## See Also

- [var title: String](nswindow/title.md)
  The string that appears in the title bar of the window or the path to the represented file.
- [var titleVisibility: NSWindow.TitleVisibility](nswindow/titlevisibility-swift.property.md)
  A value that indicates the visibility of the window’s title and title bar buttons.
- [func setTitleWithRepresentedFilename(String)](nswindow/settitlewithrepresentedfilename(_:).md)
  Sets a given path as the window’s title, formatting it as a file-system path, and records this path as the window’s associated file.
- [var representedFilename: String](nswindow/representedfilename.md)
  The path to the file of the window’s represented file.
- [var representedURL: URL?](nswindow/representedurl.md)
  The URL of the file the window represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/subtitle)*