# selectFile(_:inFileViewerRootedAtPath:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Selects the file at the specified path.

**Availability**:
- macOS

## Declaration

```swift
func selectFile(_ fullPath: String?, inFileViewerRootedAtPath rootFullPath: String) -> Bool
```

```objc
- (BOOL) selectFile:(NSString *) fullPath inFileViewerRootedAtPath:(NSString *) rootFullPath;
```

## Return Value

[`true`](../../Swift/true.md) if the file was successfully selected; otherwise, [`false`](../../Swift/false.md).

## Discussion

In macOS 10.5 and later, this method does not follow symlinks when selecting the file. If the `fullPath` parameter contains any symlinks, this method selects the symlink instead of the file it targets. If you want to select the target file, use the [`resolvingSymlinksInPath`](../../Foundation/nsstring/resolvingsymlinksinpath.md) method to resolve any symlinks before calling this method.

You can safely call this method from any thread of your app.

## Parameters

- `fullPath`: The full path of the file to select.
- `rootFullPath`: The path to use for the file viewer. If you specify a nonempty path string, this method opens a new file viewer. If you specify an empty string (`@""`), this method selects the file in the main viewer.

## See Also

### Manipulating Files
- [func duplicate([URL], completionHandler: (([URL : URL], (any Error)?) -> Void)?)](./duplicate%28_,completionhandler%29.md)
  Duplicates the specified URLS asynchronously in the same manner as the Finder.
- [func recycle([URL], completionHandler: (([URL : URL], (any Error)?) -> Void)?)](./recycle%28_,completionhandler%29.md)
  Moves the specified URLs to the trash in the same manner as the Finder.
- [func activateFileViewerSelecting([URL])](./activatefileviewerselecting%28_%29.md)
  Activates the Finder, and opens one or more windows selecting the specified files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/selectfile(_:infileviewerrootedatpath:))*