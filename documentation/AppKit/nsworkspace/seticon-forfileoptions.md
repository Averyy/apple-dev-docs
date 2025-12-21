# setIcon(_:forFile:options:)

**Framework**: AppKit  
**Kind**: method

Sets the icon for the file or directory at the specified path.

**Availability**:
- macOS ?+

## Declaration

```swift
func setIcon(_ image: NSImage?, forFile fullPath: String, options: NSWorkspace.IconCreationOptions = []) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the icon was set; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

The `image` can be an arbitrary image, with or without transparency. The method automatically scales this image (as needed) to generate the icon representations. The file or folder must exist and be writable by the user.

This method uses the image to set an icon with a size of 512 pixels by 512 pixels. If you specify the [`exclude10_4ElementsIconCreationOption`](nsworkspace/iconcreationoptions/exclude10_4elementsiconcreationoption.md) option (not recommended), this method creates an icon that is compatible with the Finder from macOS 10.2 or earlier.

You can safely call this method from any of your app’s threads, but you must call it from only one thread at a time.

## Parameters

- `image`: The image to use as the icon for the file or directory.
- `fullPath`: The full path of the file or directory.
- `options`: The icon representations to generate from the image. You specify this value by combining the appropriate   constants, using the C bitwise   operator. Specify   if you want to generate icons in all available icon representation formats.

## See Also

- [func icon(forFile: String) -> NSImage](nsworkspace/icon(forfile:).md)
  Returns an image containing the icon for the specified file.
- [func icon(forFiles: [String]) -> NSImage?](nsworkspace/icon(forfiles:).md)
  Returns an image containing the icon for the specified files.
- [func icon(for: UTType) -> NSImage](nsworkspace/icon(for:).md)
  Returns an image containing the icon for the specified content type.
- [NSWorkspace.IconCreationOptions](nsworkspace/iconcreationoptions.md)
  Constants that describe options for creating icons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/seticon(_:forfile:options:))*