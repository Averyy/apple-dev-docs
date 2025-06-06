# icon(forFiles:)

**Framework**: AppKit  
**Kind**: method

Returns an image containing the icon for the specified files.

**Availability**:
- macOS ?+

## Declaration

```swift
func icon(forFiles fullPaths: [String]) -> NSImage?
```

#### Return Value

The icon associated with the group of files.

#### Discussion

If `fullPaths` specifies one file, that file’s icon is returned. If `fullPaths` specifies more than one file, an icon representing the multiple selection is returned.

You can safely call this method from any thread of your app.

## Parameters

- `fullPaths`: An array of   objects, each of which contains the full path to a file.

## See Also

- [func icon(forFileType: String) -> NSImage](nsworkspace/icon(forfiletype:).md)
  Returns an image containing the icon for files of the specified type.
- [func icon(forFile: String) -> NSImage](nsworkspace/icon(forfile:).md)
  Returns an image containing the icon for the specified file.
- [func icon(for: UTType) -> NSImage](nsworkspace/icon(for:).md)
  Returns an image containing the icon for the specified content type.
- [func setIcon(NSImage?, forFile: String, options: NSWorkspace.IconCreationOptions) -> Bool](nsworkspace/seticon(_:forfile:options:).md)
  Sets the icon for the file or directory at the specified path.
- [NSWorkspace.IconCreationOptions](nsworkspace/iconcreationoptions.md)
  Constants that describe options for creating icons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/icon(forfiles:))*