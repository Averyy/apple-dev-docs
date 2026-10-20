# runModalOpenPanel(_:forTypes:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Presents a modal Open dialog and limits selection to specific file types.

**Availability**:
- macOS

## Declaration

```swift
func runModalOpenPanel(_ openPanel: NSOpenPanel, forTypes types: [String]?) -> Int
```

```objc
- (NSInteger) runModalOpenPanel:(NSOpenPanel *) openPanel forTypes:(NSArray<NSString *> *) types;
```

#### Discussion

This method is called by the [`urlsFromRunningOpenPanel()`](./urlsfromrunningopenpanel%28%29.md) method. It calls the `NSOpenPanel` [`runModalForTypes:`](../nsopenpanel/runmodalfortypes_.md) method, passing the `openPanel` object and the file extensions associated with a document type. The `extensions` parameter may also contain encoded HFS file types as well as filename extensions.

## Parameters

- `openPanel`: The open panel to display.
- `types`: An array of allowable types to open.

## See Also

### Managing the Open Dialog
- [func beginOpenPanel(completionHandler: ([URL]?) -> Void)](./beginopenpanel%28completionhandler%29.md)
  Presents an Open dialog and delivers the results to a completion handler as an array of URLs for the chosen files, or nil.
- [func beginOpenPanel(NSOpenPanel, forTypes: [String]?, completionHandler: (Int) -> Void)](./beginopenpanel%28_,fortypes,completionhandler%29.md)
  Presents a nonmodal Open dialog that displays files you can open from a list of UTIs.
- [var currentDirectory: String?](./currentdirectory.md)
  The directory path to use as the starting point in the Open dialog.
- [func urlsFromRunningOpenPanel() -> [URL]?](./urlsfromrunningopenpanel%28%29.md)
  An array of URLs that correspond to the selected files in a running Open dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/runmodalopenpanel(_:fortypes:))*