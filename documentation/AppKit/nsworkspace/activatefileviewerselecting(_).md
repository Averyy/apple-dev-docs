# activateFileViewerSelecting(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Activates the Finder, and opens one or more windows selecting the specified files.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func activateFileViewerSelecting(_ fileURLs: [URL])
```

```objc
- (void) activateFileViewerSelectingURLs:(NSArray<NSURL *> *) fileURLs;
```

#### Discussion

You can safely call this method from any thread of your app.

## Parameters

- `fileURLs`: The files to select and display in the Finder.

## See Also

### Manipulating Files
- [func duplicate([URL], completionHandler: (([URL : URL], (any Error)?) -> Void)?)](./duplicate%28_,completionhandler%29.md)
  Duplicates the specified URLS asynchronously in the same manner as the Finder.
- [func recycle([URL], completionHandler: (([URL : URL], (any Error)?) -> Void)?)](./recycle%28_,completionhandler%29.md)
  Moves the specified URLs to the trash in the same manner as the Finder.
- [func selectFile(String?, inFileViewerRootedAtPath: String) -> Bool](./selectfile%28_,infileviewerrootedatpath%29.md)
  Selects the file at the specified path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/activatefileviewerselecting(_:))*