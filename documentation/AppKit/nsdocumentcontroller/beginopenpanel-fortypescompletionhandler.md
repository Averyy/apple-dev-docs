# beginOpenPanel(_:forTypes:completionHandler:)

**Framework**: AppKit  
**Kind**: method

Presents a nonmodal Open dialog that displays files you can open from a list of UTIs.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
func beginOpenPanel(_ openPanel: NSOpenPanel, forTypes inTypes: [String]?) async -> Int
```

#### Discussion

[`openDocument(_:)`](nsdocumentcontroller/opendocument(_:).md) and [`beginOpenPanel(completionHandler:)`](nsdocumentcontroller/beginopenpanel(completionhandler:).md) call this method to do the actual work. You typically don’t call this method directly. Override this method as necessary to customize the Open dialog or to alter the list of UTIs in the `inTypes` parameter.

You can also override this method if you want to perform additional cleanup (for example, if you customize the Open dialog and need to tear down an accessory view). Your overridden implementation needs to call the underlying method on `super`, passing a custom completion handler. That handler does the additional cleanup work, and then calls the completion handler block that the caller provides.

## Parameters

- `openPanel`: The Open dialog to present.
- `inTypes`: A list of file types that the user can choose from in the Open dialog.
- `completionHandler`: The block takes the following parameter:

## See Also

- [func beginOpenPanel(completionHandler: ([URL]?) -> Void)](nsdocumentcontroller/beginopenpanel(completionhandler:).md)
  Presents an Open dialog and delivers the results to a completion handler as an array of URLs for the chosen files (or `nil`).
- [func runModalOpenPanel(NSOpenPanel, forTypes: [String]?) -> Int](nsdocumentcontroller/runmodalopenpanel(_:fortypes:).md)
  Presents a modal Open dialog and limits selection to specific file types.
- [var currentDirectory: String?](nsdocumentcontroller/currentdirectory.md)
  The directory path to be used as the starting point in the Open panel.
- [func urlsFromRunningOpenPanel() -> [URL]?](nsdocumentcontroller/urlsfromrunningopenpanel.md)
  An array of URLs corresponding to the files selected in a running open panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/beginopenpanel(_:fortypes:completionhandler:))*