# icon(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns an image containing the icon for the specified content type.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func icon(for contentType: UTType) -> NSImage
```

```objc
- (NSImage *) iconForContentType:(UTType *) contentType;
```

#### Return Value

The icon associated with the content type.

#### Discussion

This method returns a default icon if the operation fails.

## Parameters

- `contentType`: An object representing a uniform type of content.

## See Also

### Managing Icons
- [func icon(forFile: String) -> NSImage](./icon%28forfile%29.md)
  Returns an image containing the icon for the specified file.
- [func icon(forFiles: [String]) -> NSImage?](./icon%28forfiles%29.md)
  Returns an image containing the icon for the specified files.
- [func setIcon(NSImage?, forFile: String, options: NSWorkspace.IconCreationOptions) -> Bool](./seticon%28_,forfile,options%29.md)
  Sets the icon for the file or directory at the specified path.
- [NSWorkspace.IconCreationOptions](./iconcreationoptions.md)
  Constants that describe options for creating icons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/icon(for:))*