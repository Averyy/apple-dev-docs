# urlsFromRunningOpenPanel()

**Framework**: AppKit  
**Kind**: method

An array of URLs that correspond to the selected files in a running Open dialog.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func urlsFromRunningOpenPanel() -> [URL]?
```

#### Discussion

Accessing this property creates an [`NSOpenPanel`](nsopenpanel.md) object and runs it using the [`runModalOpenPanel(_:forTypes:)`](nsdocumentcontroller/runmodalopenpanel(_:fortypes:).md) method. When the user dismisses the panel, the returned value is an array of URLs corresponding to the files chosen by the user. The value is `nil` if the user cancels the Open panel or makes no selection.

## See Also

- [func beginOpenPanel(completionHandler: ([URL]?) -> Void)](nsdocumentcontroller/beginopenpanel(completionhandler:).md)
  Presents an Open dialog and delivers the results to a completion handler as an array of URLs for the chosen files, or nil.
- [func beginOpenPanel(NSOpenPanel, forTypes: [String]?, completionHandler: (Int) -> Void)](nsdocumentcontroller/beginopenpanel(_:fortypes:completionhandler:).md)
  Presents a nonmodal Open dialog that displays files you can open from a list of UTIs.
- [func runModalOpenPanel(NSOpenPanel, forTypes: [String]?) -> Int](nsdocumentcontroller/runmodalopenpanel(_:fortypes:).md)
  Presents a modal Open dialog and limits selection to specific file types.
- [var currentDirectory: String?](nsdocumentcontroller/currentdirectory.md)
  The directory path to use as the starting point in the Open dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/urlsfromrunningopenpanel())*