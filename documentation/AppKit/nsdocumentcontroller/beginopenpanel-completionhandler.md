# beginOpenPanel(completionHandler:)

**Framework**: AppKit  
**Kind**: method

Presents an Open dialog and delivers the results to a completion handler as an array of URLs for the chosen files, or nil.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
func beginOpenPanel() async -> [URL]?
```

#### Discussion

This method presents either a modal or nonmodal open panel, depending on which methods are overridden. Although you can call this method in other circumstances, this method is most commonly called by [`openDocument(_:)`](nsdocumentcontroller/opendocument(_:).md) in response to the user choosing Open… from the File menu.

If you override [`openDocument(_:)`](nsdocumentcontroller/opendocument(_:).md), you should typically call this method instead of calling [`beginOpenPanel(_:forTypes:completionHandler:)`](nsdocumentcontroller/beginopenpanel(_:fortypes:completionhandler:).md) or [`urlsFromRunningOpenPanel()`](nsdocumentcontroller/urlsfromrunningopenpanel().md) directly, because this method runs the modal panel in a way that is backwards compatible with subclasses that override [`runModalOpenPanel(_:forTypes:)`](nsdocumentcontroller/runmodalopenpanel(_:fortypes:).md) without overriding [`beginOpenPanel(_:forTypes:completionHandler:)`](nsdocumentcontroller/beginopenpanel(_:fortypes:completionhandler:).md). Also, its completion handler determines which button the user pressed (to determine whether to return the array or `nil`) and orders out the open panel.

You can override this method to change the open panel presentation (adding an accessory view, for example) or change the UTI array that limits which files are selectable.

The default implementation of this method calls either [`urlsFromRunningOpenPanel()`](nsdocumentcontroller/urlsfromrunningopenpanel().md) to run a modal open panel or [`beginOpenPanel(_:forTypes:completionHandler:)`](nsdocumentcontroller/beginopenpanel(_:fortypes:completionhandler:).md) to begin a nonmodal open panel. If the user chooses to open files, the default implementation calls the completion handler with a `nil` array parameter. If the user cancels the Open dialog, the default implementation calls the completion handler with a `nil` array parameter.

If you override this method, your method should typically call the underlying method on `super` because of the additional code that it provides for free. Specifically, this method runs the modal panel in a way that is backwards compatible with subclasses that override [`runModalOpenPanel(_:forTypes:)`](nsdocumentcontroller/runmodalopenpanel(_:fortypes:).md) without overriding [`beginOpenPanel(_:forTypes:completionHandler:)`](nsdocumentcontroller/beginopenpanel(_:fortypes:completionhandler:).md). Also, its completion handler determines which button the user pressed (to determine whether to return the array or `nil`) and orders out the open panel.

## Parameters

- `completionHandler`: The completion handler that is called when the user clicks the OK or Cancel button in the open panel.

## See Also

- [func beginOpenPanel(NSOpenPanel, forTypes: [String]?, completionHandler: (Int) -> Void)](nsdocumentcontroller/beginopenpanel(_:fortypes:completionhandler:).md)
  Presents a nonmodal Open dialog that displays files you can open from a list of UTIs.
- [func runModalOpenPanel(NSOpenPanel, forTypes: [String]?) -> Int](nsdocumentcontroller/runmodalopenpanel(_:fortypes:).md)
  Presents a modal Open dialog and limits selection to specific file types.
- [var currentDirectory: String?](nsdocumentcontroller/currentdirectory.md)
  The directory path to use as the starting point in the Open dialog.
- [func urlsFromRunningOpenPanel() -> [URL]?](nsdocumentcontroller/urlsfromrunningopenpanel.md)
  An array of URLs that correspond to the selected files in a running Open dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/beginopenpanel(completionhandler:))*