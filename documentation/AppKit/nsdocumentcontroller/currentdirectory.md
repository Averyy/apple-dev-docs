# currentDirectory

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The directory path to use as the starting point in the Open dialog.

**Availability**:
- macOS

## Declaration

```swift
var currentDirectory: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * currentDirectory;
```

## Discussion

The first valid directory from the following list is returned:

- The directory location where the current document was last saved
- The last directory visited in the Open panel
- The user’s home directory

## See Also

### Managing the Open Dialog
- [func beginOpenPanel(completionHandler: ([URL]?) -> Void)](./beginopenpanel%28completionhandler%29.md)
  Presents an Open dialog and delivers the results to a completion handler as an array of URLs for the chosen files, or nil.
- [func beginOpenPanel(NSOpenPanel, forTypes: [String]?, completionHandler: (Int) -> Void)](./beginopenpanel%28_,fortypes,completionhandler%29.md)
  Presents a nonmodal Open dialog that displays files you can open from a list of UTIs.
- [func runModalOpenPanel(NSOpenPanel, forTypes: [String]?) -> Int](./runmodalopenpanel%28_,fortypes%29.md)
  Presents a modal Open dialog and limits selection to specific file types.
- [func urlsFromRunningOpenPanel() -> [URL]?](./urlsfromrunningopenpanel%28%29.md)
  An array of URLs that correspond to the selected files in a running Open dialog.
### Related Documentation
- [- documentForFileName:](./documentforfilename_.md)
  Returns the document object for the file in which the document data is stored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/currentdirectory)*