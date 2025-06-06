# representedURL

**Framework**: AppKit  
**Kind**: property

The URL of the file the window represents.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
var representedURL: URL? { get set }
```

#### Discussion

When the URL specifies a path, the window shows an icon in its title bar, as described in the following table:

| File path | Document icon |
| --- | --- |
| Empty | None |
| Specifies a nonexistent file | Generic |
| Specifies an existent file | Specific for the file’s type |

You can customize the file icon in the title bar with the following code:

```objc
[[<window> standardWindowButton:NSWindowDocumentIconButton] setImage:<image>]
```

When the URL identifies an existing file, the window’s title offers a pop-up menu showing the path components of the URL. (The user displays this menu by Command-clicking the title.) The behavior and contents of this menu can be controlled with [`window(_:shouldPopUpDocumentPathMenu:)`](nswindowdelegate/window(_:shouldpopupdocumentpathmenu:).md).

## See Also

- [func window(NSWindow, shouldDragDocumentWith: NSEvent, from: NSPoint, with: NSPasteboard) -> Bool](nswindowdelegate/window(_:shoulddragdocumentwith:from:with:).md)
  Asks the delegate whether a user can drag the document icon from the window’s title bar.
- [var title: String](nswindow/title.md)
  The string that appears in the title bar of the window or the path to the represented file.
- [var subtitle: String](nswindow/subtitle.md)
  A secondary line of text that appears in the title bar of the window.
- [var titleVisibility: NSWindow.TitleVisibility](nswindow/titlevisibility-swift.property.md)
  A value that indicates the visibility of the window’s title and title bar buttons.
- [func setTitleWithRepresentedFilename(String)](nswindow/settitlewithrepresentedfilename(_:).md)
  Sets a given path as the window’s title, formatting it as a file-system path, and records this path as the window’s associated file.
- [var representedFilename: String](nswindow/representedfilename.md)
  The path to the file of the window’s represented file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/representedurl)*