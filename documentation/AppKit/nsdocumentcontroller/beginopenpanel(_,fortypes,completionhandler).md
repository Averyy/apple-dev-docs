# beginOpenPanel(_:forTypes:completionHandler:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Presents a nonmodal Open dialog that displays files you can open from a list of UTIs.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func beginOpenPanel(_ openPanel: NSOpenPanel, forTypes inTypes: [String]?, completionHandler: @escaping (Int) -> Void)
```

```swift
func beginOpenPanel(_ openPanel: NSOpenPanel, forTypes inTypes: [String]?) async -> Int
```

```objc
- (void) beginOpenPanel:(NSOpenPanel *) openPanel forTypes:(NSArray<NSString *> *) inTypes completionHandler:(void (^)(NSInteger result)) completionHandler;
```

## Discussion

[`openDocument(_:)`](./opendocument%28_%29.md) and [`beginOpenPanel(completionHandler:)`](./beginopenpanel%28completionhandler%29.md) call this method to do the actual work. You typically don’t call this method directly. Override this method as necessary to customize the Open dialog or to alter the list of UTIs in the `inTypes` parameter.

You can also override this method if you want to perform additional cleanup (for example, if you customize the Open dialog and need to tear down an accessory view). Your overridden implementation needs to call the underlying method on `super`, passing a custom completion handler. That handler does the additional cleanup work, and then calls the completion handler block that the caller provides.

## Parameters

- `openPanel`: The Open dialog to present.
- `inTypes`: A list of file types that the user can choose from in the Open dialog.
- `completionHandler`: The completion handler that runs when the user clicks the OK or Cancel button in the Open dialog.

  The block takes the following parameter:

  - **`result`**: Either [`NSOKButton`](../nsokbutton.md) or [`NSCancelButton`](../nscancelbutton.md), depending on which button the user clicks to dismiss the dialog.

## See Also

### Managing the Open Dialog
- [func beginOpenPanel(completionHandler: ([URL]?) -> Void)](./beginopenpanel%28completionhandler%29.md)
  Presents an Open dialog and delivers the results to a completion handler as an array of URLs for the chosen files, or nil.
- [func runModalOpenPanel(NSOpenPanel, forTypes: [String]?) -> Int](./runmodalopenpanel%28_,fortypes%29.md)
  Presents a modal Open dialog and limits selection to specific file types.
- [var currentDirectory: String?](./currentdirectory.md)
  The directory path to use as the starting point in the Open dialog.
- [func urlsFromRunningOpenPanel() -> [URL]?](./urlsfromrunningopenpanel%28%29.md)
  An array of URLs that correspond to the selected files in a running Open dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/beginopenpanel(_:fortypes:completionhandler:))*