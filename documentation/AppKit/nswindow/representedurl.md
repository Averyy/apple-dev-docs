# representedURL

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The URL of the file the window represents.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var representedURL: URL? { get set }
```

```objc
@property (copy, nullable) NSURL * representedURL;
```

## Discussion

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

When the URL identifies an existing file, the window’s title offers a pop-up menu showing the path components of the URL. (The user displays this menu by Command-clicking the title.) The behavior and contents of this menu can be controlled with [`window(_:shouldPopUpDocumentPathMenu:)`](../nswindowdelegate/window%28_,shouldpopupdocumentpathmenu%29.md).

## See Also

### Related Documentation
- [func window(NSWindow, shouldDragDocumentWith: NSEvent, from: NSPoint, with: NSPasteboard) -> Bool](../nswindowdelegate/window%28_,shoulddragdocumentwith,from,with%29.md)
  Asks the delegate whether a user can drag the document icon from the window’s title bar.
### Managing Titles
- [var title: String](./title.md)
  The string that appears in the title bar of the window or the path to the represented file.
- [var subtitle: String](./subtitle.md)
  A secondary line of text that appears in the title bar of the window.
- [var titleVisibility: NSWindow.TitleVisibility](./titlevisibility-swift.property.md)
  A value that indicates the visibility of the window’s title and title bar buttons.
- [func setTitleWithRepresentedFilename(String)](./settitlewithrepresentedfilename%28_%29.md)
  Sets a given path as the window’s title, formatting it as a file-system path, and records this path as the window’s associated file.
- [var representedFilename: String](./representedfilename.md)
  The path to the file of the window’s represented file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/representedurl)*