# runModalOpenPanel(_:forTypes:)

**Framework**: AppKit  
**Kind**: method

Presents a modal Open dialog and limits selection to specific file types.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func runModalOpenPanel(_ openPanel: NSOpenPanel, forTypes types: [String]?) -> Int
```

#### Discussion

This method is called by the [`urlsFromRunningOpenPanel()`](nsdocumentcontroller/urlsfromrunningopenpanel().md) method. It calls the `NSOpenPanel` [`runModalForTypes:`](nsopenpanel/runmodalfortypes:.md) method, passing the `openPanel` object and the file extensions associated with a document type. The `extensions` parameter may also contain encoded HFS file types as well as filename extensions.

## Parameters

- `openPanel`: The open panel to display.
- `types`: An array of allowable types to open.

## See Also

- [func beginOpenPanel(completionHandler: ([URL]?) -> Void)](nsdocumentcontroller/beginopenpanel(completionhandler:).md)
  Presents an Open dialog and delivers the results to a completion handler as an array of URLs for the chosen files, or nil.
- [func beginOpenPanel(NSOpenPanel, forTypes: [String]?, completionHandler: (Int) -> Void)](nsdocumentcontroller/beginopenpanel(_:fortypes:completionhandler:).md)
  Presents a nonmodal Open dialog that displays files you can open from a list of UTIs.
- [var currentDirectory: String?](nsdocumentcontroller/currentdirectory.md)
  The directory path to use as the starting point in the Open dialog.
- [func urlsFromRunningOpenPanel() -> [URL]?](nsdocumentcontroller/urlsfromrunningopenpanel.md)
  An array of URLs that correspond to the selected files in a running Open dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/runmodalopenpanel(_:fortypes:))*