# urlsFromRunningOpenPanel()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

An array of URLs that correspond to the selected files in a running Open dialog.

**Availability**:
- macOS

## Declaration

```swift
func urlsFromRunningOpenPanel() -> [URL]?
```

```objc
- (NSArray<NSURL *> *) URLsFromRunningOpenPanel;
```

#### Discussion

Accessing this property creates an [`NSOpenPanel`](../nsopenpanel.md) object and runs it using the [`runModalOpenPanel(_:forTypes:)`](./runmodalopenpanel%28_,fortypes%29.md) method. When the user dismisses the panel, the returned value is an array of URLs corresponding to the files chosen by the user. The value is `nil` if the user cancels the Open panel or makes no selection.

## See Also

### Managing the Open Dialog
- [func beginOpenPanel(completionHandler: ([URL]?) -> Void)](./beginopenpanel%28completionhandler%29.md)
  Presents an Open dialog and delivers the results to a completion handler as an array of URLs for the chosen files, or nil.
- [func beginOpenPanel(NSOpenPanel, forTypes: [String]?, completionHandler: (Int) -> Void)](./beginopenpanel%28_,fortypes,completionhandler%29.md)
  Presents a nonmodal Open dialog that displays files you can open from a list of UTIs.
- [func runModalOpenPanel(NSOpenPanel, forTypes: [String]?) -> Int](./runmodalopenpanel%28_,fortypes%29.md)
  Presents a modal Open dialog and limits selection to specific file types.
- [var currentDirectory: String?](./currentdirectory.md)
  The directory path to use as the starting point in the Open dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/urlsfromrunningopenpanel())*