# setTitleWithRepresentedFilename(_:)

**Framework**: AppKit  
**Kind**: method

Sets a given path as the window’s title, formatting it as a file-system path, and records this path as the window’s associated file.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setTitleWithRepresentedFilename(_ filename: String)
```

#### Discussion

The windows’ title bar displays the filename, not the file’s path.

## Parameters

- `filename`: The file path to set as the window’s title.

## See Also

- [var miniwindowTitle: String!](nswindow/miniwindowtitle.md)
  The title displayed in the window’s minimized window.
- [var title: String](nswindow/title.md)
  The string that appears in the title bar of the window or the path to the represented file.
- [var subtitle: String](nswindow/subtitle.md)
  A secondary line of text that appears in the title bar of the window.
- [var titleVisibility: NSWindow.TitleVisibility](nswindow/titlevisibility-swift.property.md)
  A value that indicates the visibility of the window’s title and title bar buttons.
- [var representedFilename: String](nswindow/representedfilename.md)
  The path to the file of the window’s represented file.
- [var representedURL: URL?](nswindow/representedurl.md)
  The URL of the file the window represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/settitlewithrepresentedfilename(_:))*