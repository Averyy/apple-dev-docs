# subtitle

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A secondary line of text that appears in the title bar of the window.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var subtitle: String { get set }
```

```objc
@property (copy) NSString * subtitle;
```

## Discussion

When this property is an empty string, the system removes the subtitle from the window layout.

> **Note**:  When you present a window as a sheet, the window never displays this subtitle, regardless of its value.

## See Also

### Managing Titles
- [var title: String](./title.md)
  The string that appears in the title bar of the window or the path to the represented file.
- [var titleVisibility: NSWindow.TitleVisibility](./titlevisibility-swift.property.md)
  A value that indicates the visibility of the window’s title and title bar buttons.
- [func setTitleWithRepresentedFilename(String)](./settitlewithrepresentedfilename%28_%29.md)
  Sets a given path as the window’s title, formatting it as a file-system path, and records this path as the window’s associated file.
- [var representedFilename: String](./representedfilename.md)
  The path to the file of the window’s represented file.
- [var representedURL: URL?](./representedurl.md)
  The URL of the file the window represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/subtitle)*