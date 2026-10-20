# titleVisibility

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A value that indicates the visibility of the window’s title and title bar buttons.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var titleVisibility: NSWindow.TitleVisibility { get set }
```

```objc
@property NSWindowTitleVisibility titleVisibility;
```

#### Discussion

By default, the value of this property is [`NSWindow.TitleVisibility.visible`](./titlevisibility-swift.enum/visible.md).

> **Note**:  When you present a window as a sheet, the window never displays a title, regardless of this property or the window’s [`title`](./title.md) string. The [`titled`](./stylemask-swift.struct/titled.md) style mask flag still affects other behavior, such as the default value of [`canBecomeKey`](./canbecomekey.md), even though it doesn’t cause a sheet to display a title.

## See Also

### Managing Titles
- [var title: String](./title.md)
  The string that appears in the title bar of the window or the path to the represented file.
- [var subtitle: String](./subtitle.md)
  A secondary line of text that appears in the title bar of the window.
- [func setTitleWithRepresentedFilename(String)](./settitlewithrepresentedfilename%28_%29.md)
  Sets a given path as the window’s title, formatting it as a file-system path, and records this path as the window’s associated file.
- [var representedFilename: String](./representedfilename.md)
  The path to the file of the window’s represented file.
- [var representedURL: URL?](./representedurl.md)
  The URL of the file the window represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/titlevisibility-swift.property)*