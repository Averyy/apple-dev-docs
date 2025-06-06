# icon(forFile:)

**Framework**: AppKit  
**Kind**: method

Returns an image containing the icon for the specified file.

**Availability**:
- macOS ?+

## Declaration

```swift
func icon(forFile fullPath: String) -> NSImage
```

#### Return Value

The icon associated with the file.

#### Discussion

The returned image has an initial size of 32 pixels by 32 pixels.

You can safely call this method from any thread of your app.

## Parameters

- `fullPath`: The full path to the file.

## See Also

- [func icon(forFileType: String) -> NSImage](nsworkspace/icon(forfiletype:).md)
  Returns an image containing the icon for files of the specified type.
- [func getInfoForFile(String, application: AutoreleasingUnsafeMutablePointer<NSString?>?, type: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](nsworkspace/getinfoforfile(_:application:type:).md)
  Retrieves information about the specified file.
- [func icon(forFiles: [String]) -> NSImage?](nsworkspace/icon(forfiles:).md)
  Returns an image containing the icon for the specified files.
- [func icon(for: UTType) -> NSImage](nsworkspace/icon(for:).md)
  Returns an image containing the icon for the specified content type.
- [func setIcon(NSImage?, forFile: String, options: NSWorkspace.IconCreationOptions) -> Bool](nsworkspace/seticon(_:forfile:options:).md)
  Sets the icon for the file or directory at the specified path.
- [NSWorkspace.IconCreationOptions](nsworkspace/iconcreationoptions.md)
  Constants that describe options for creating icons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/icon(forfile:))*