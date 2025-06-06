# icon(for:)

**Framework**: AppKit  
**Kind**: method

Returns an image containing the icon for the specified content type.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func icon(for contentType: UTType) -> NSImage
```

#### Return Value

The icon associated with the content type.

#### Discussion

This method returns a default icon if the operation fails.

## Parameters

- `contentType`: An object representing a uniform type of content.

## See Also

- [func icon(forFile: String) -> NSImage](nsworkspace/icon(forfile:).md)
  Returns an image containing the icon for the specified file.
- [func icon(forFiles: [String]) -> NSImage?](nsworkspace/icon(forfiles:).md)
  Returns an image containing the icon for the specified files.
- [func setIcon(NSImage?, forFile: String, options: NSWorkspace.IconCreationOptions) -> Bool](nsworkspace/seticon(_:forfile:options:).md)
  Sets the icon for the file or directory at the specified path.
- [NSWorkspace.IconCreationOptions](nsworkspace/iconcreationoptions.md)
  Constants that describe options for creating icons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/icon(for:))*