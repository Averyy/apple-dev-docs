# activateFileViewerSelecting(_:)

**Framework**: AppKit  
**Kind**: method

Activates the Finder, and opens one or more windows selecting the specified files.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func activateFileViewerSelecting(_ fileURLs: [URL])
```

#### Discussion

You can safely call this method from any thread of your app.

## Parameters

- `fileURLs`: The files to select and display in the Finder.

## See Also

- [func duplicate([URL], completionHandler: (([URL : URL], (any Error)?) -> Void)?)](nsworkspace/duplicate(_:completionhandler:).md)
  Duplicates the specified URLS asynchronously in the same manner as the Finder.
- [func recycle([URL], completionHandler: (([URL : URL], (any Error)?) -> Void)?)](nsworkspace/recycle(_:completionhandler:).md)
  Moves the specified URLs to the trash in the same manner as the Finder.
- [func selectFile(String?, inFileViewerRootedAtPath: String) -> Bool](nsworkspace/selectfile(_:infileviewerrootedatpath:).md)
  Selects the file at the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/activatefileviewerselecting(_:))*