# duplicate(_:completionHandler:)

**Framework**: AppKit  
**Kind**: method

Duplicates the specified URLS asynchronously in the same manner as the Finder.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func duplicate(_ URLs: [URL]) async throws -> [URL : URL]
```

#### Discussion

This method may cause a progress indicator, or other user interface element, to be shown by the Finder.

In macOS 10.6, this method requires the app to run its main run loop in a common mode. You can safely call this method from any thread of your app.

## Parameters

- `URLs`: An array of   objects representing the files to duplicate. This parameter must not be  .
- `handler`: This block takes two parameters:

## See Also

- [func recycle([URL], completionHandler: (([URL : URL], (any Error)?) -> Void)?)](nsworkspace/recycle(_:completionhandler:).md)
  Moves the specified URLs to the trash in the same manner as the Finder.
- [func activateFileViewerSelecting([URL])](nsworkspace/activatefileviewerselecting(_:).md)
  Activates the Finder, and opens one or more windows selecting the specified files.
- [func selectFile(String?, inFileViewerRootedAtPath: String) -> Bool](nsworkspace/selectfile(_:infileviewerrootedatpath:).md)
  Selects the file at the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/duplicate(_:completionhandler:))*