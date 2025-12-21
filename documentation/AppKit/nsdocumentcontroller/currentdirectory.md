# currentDirectory

**Framework**: AppKit  
**Kind**: property

The directory path to use as the starting point in the Open dialog.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var currentDirectory: String? { get }
```

#### Discussion

The first valid directory from the following list is returned:

- The directory location where the current document was last saved
- The last directory visited in the Open panel
- The user’s home directory

## See Also

- [func beginOpenPanel(completionHandler: ([URL]?) -> Void)](nsdocumentcontroller/beginopenpanel(completionhandler:).md)
  Presents an Open dialog and delivers the results to a completion handler as an array of URLs for the chosen files, or nil.
- [func beginOpenPanel(NSOpenPanel, forTypes: [String]?, completionHandler: (Int) -> Void)](nsdocumentcontroller/beginopenpanel(_:fortypes:completionhandler:).md)
  Presents a nonmodal Open dialog that displays files you can open from a list of UTIs.
- [func runModalOpenPanel(NSOpenPanel, forTypes: [String]?) -> Int](nsdocumentcontroller/runmodalopenpanel(_:fortypes:).md)
  Presents a modal Open dialog and limits selection to specific file types.
- [func urlsFromRunningOpenPanel() -> [URL]?](nsdocumentcontroller/urlsfromrunningopenpanel.md)
  An array of URLs that correspond to the selected files in a running Open dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/currentdirectory)*