# icon(forFiles:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns an image containing the icon for the specified files.

**Availability**:
- macOS

## Declaration

```swift
func icon(forFiles fullPaths: [String]) -> NSImage?
```

```objc
- (NSImage *) iconForFiles:(NSArray<NSString *> *) fullPaths;
```

## Return Value

The icon associated with the group of files.

## Discussion

If `fullPaths` specifies one file, that file’s icon is returned. If `fullPaths` specifies more than one file, an icon representing the multiple selection is returned.

You can safely call this method from any thread of your app.

## Parameters

- `fullPaths`: An array of `NSString` objects, each of which contains the full path to a file.

## See Also

### Related Documentation
- [func icon(forFileType: String) -> NSImage](./icon%28forfiletype%29.md)
  Returns an image containing the icon for files of the specified type.
### Managing Icons
- [func icon(forFile: String) -> NSImage](./icon%28forfile%29.md)
  Returns an image containing the icon for the specified file.
- [func icon(for: UTType) -> NSImage](./icon%28for%29.md)
  Returns an image containing the icon for the specified content type.
- [func setIcon(NSImage?, forFile: String, options: NSWorkspace.IconCreationOptions) -> Bool](./seticon%28_,forfile,options%29.md)
  Sets the icon for the file or directory at the specified path.
- [NSWorkspace.IconCreationOptions](./iconcreationoptions.md)
  Constants that describe options for creating icons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/icon(forfiles:))*