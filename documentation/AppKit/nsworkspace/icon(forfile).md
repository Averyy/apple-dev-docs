# icon(forFile:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns an image containing the icon for the specified file.

**Availability**:
- macOS

## Declaration

```swift
func icon(forFile fullPath: String) -> NSImage
```

```objc
- (NSImage *) iconForFile:(NSString *) fullPath;
```

#### Return Value

The icon associated with the file.

#### Discussion

The returned image has an initial size of 32 pixels by 32 pixels.

You can safely call this method from any thread of your app.

## Parameters

- `fullPath`: The full path to the file.

## See Also

### Related Documentation
- [func icon(forFileType: String) -> NSImage](./icon%28forfiletype%29.md)
  Returns an image containing the icon for files of the specified type.
- [func getInfoForFile(String, application: AutoreleasingUnsafeMutablePointer<NSString?>?, type: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](./getinfoforfile%28_,application,type%29.md)
  Retrieves information about the specified file.
### Managing Icons
- [func icon(forFiles: [String]) -> NSImage?](./icon%28forfiles%29.md)
  Returns an image containing the icon for the specified files.
- [func icon(for: UTType) -> NSImage](./icon%28for%29.md)
  Returns an image containing the icon for the specified content type.
- [func setIcon(NSImage?, forFile: String, options: NSWorkspace.IconCreationOptions) -> Bool](./seticon%28_,forfile,options%29.md)
  Sets the icon for the file or directory at the specified path.
- [NSWorkspace.IconCreationOptions](./iconcreationoptions.md)
  Constants that describe options for creating icons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/icon(forfile:))*