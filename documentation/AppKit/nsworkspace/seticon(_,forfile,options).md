# setIcon(_:forFile:options:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the icon for the file or directory at the specified path.

**Availability**:
- macOS

## Declaration

```swift
func setIcon(_ image: NSImage?, forFile fullPath: String, options: NSWorkspace.IconCreationOptions = []) -> Bool
```

```objc
- (BOOL) setIcon:(NSImage *) image forFile:(NSString *) fullPath options:(NSWorkspaceIconCreationOptions) options;
```

## Return Value

[`true`](../../Swift/true.md) if the icon was set; otherwise, [`false`](../../Swift/false.md).

## Discussion

The `image` can be an arbitrary image, with or without transparency. The method automatically scales this image (as needed) to generate the icon representations. The file or folder must exist and be writable by the user.

This method uses the image to set an icon with a size of 512 pixels by 512 pixels. If you specify the [`exclude10_4ElementsIconCreationOption`](./iconcreationoptions/exclude10_4elementsiconcreationoption.md) option (not recommended), this method creates an icon that is compatible with the Finder from macOS 10.2 or earlier.

You can safely call this method from any of your app’s threads, but you must call it from only one thread at a time.

## Parameters

- `image`: The image to use as the icon for the file or directory.
- `fullPath`: The full path of the file or directory.
- `options`: The icon representations to generate from the image. You specify this value by combining the appropriate [`NSWorkspace.IconCreationOptions`](./iconcreationoptions.md) constants, using the C bitwise `OR` operator. Specify `0` if you want to generate icons in all available icon representation formats.

## See Also

### Managing Icons
- [func icon(forFile: String) -> NSImage](./icon%28forfile%29.md)
  Returns an image containing the icon for the specified file.
- [func icon(forFiles: [String]) -> NSImage?](./icon%28forfiles%29.md)
  Returns an image containing the icon for the specified files.
- [func icon(for: UTType) -> NSImage](./icon%28for%29.md)
  Returns an image containing the icon for the specified content type.
- [NSWorkspace.IconCreationOptions](./iconcreationoptions.md)
  Constants that describe options for creating icons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/seticon(_:forfile:options:))*