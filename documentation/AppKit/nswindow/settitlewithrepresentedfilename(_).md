# setTitleWithRepresentedFilename(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets a given path as the window’s title, formatting it as a file-system path, and records this path as the window’s associated file.

**Availability**:
- macOS

## Declaration

```swift
func setTitleWithRepresentedFilename(_ filename: String)
```

```objc
- (void) setTitleWithRepresentedFilename:(NSString *) filename;
```

## Discussion

The windows’ title bar displays the filename, not the file’s path.

## Parameters

- `filename`: The file path to set as the window’s title.

## See Also

### Related Documentation
- [var miniwindowTitle: String!](./miniwindowtitle.md)
  The title displayed in the window’s minimized window.
### Managing Titles
- [var title: String](./title.md)
  The string that appears in the title bar of the window or the path to the represented file.
- [var subtitle: String](./subtitle.md)
  A secondary line of text that appears in the title bar of the window.
- [var titleVisibility: NSWindow.TitleVisibility](./titlevisibility-swift.property.md)
  A value that indicates the visibility of the window’s title and title bar buttons.
- [var representedFilename: String](./representedfilename.md)
  The path to the file of the window’s represented file.
- [var representedURL: URL?](./representedurl.md)
  The URL of the file the window represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/settitlewithrepresentedfilename(_:))*