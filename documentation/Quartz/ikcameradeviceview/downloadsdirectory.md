# downloadsDirectory

**Framework**: Quartz  
**Kind**: property  
**Role**: Instance Property

Specifies the directory where files are downloaded

**Availability**:
- macOS 10.6+

## Declaration

```swift
var downloadsDirectory: URL! { get set }
```

```objc
@property (retain) NSURL * downloadsDirectory;
```

## See Also

### Configuring Download Interface and Downloading Files
- [var canDownloadSelectedItems: Bool](./candownloadselecteditems.md)
  Returns whether the selected items can be downloaded
- [func downloadSelectedItems(Any!)](./downloadselecteditems%28_%29.md)
  Deletes the selected items from the camera.
- [func downloadAllItems(Any!)](./downloadallitems%28_%29.md)
  Downloads all the items.
- [var downloadSelectedControlLabel: String!](./downloadselectedcontrollabel.md)
  Allows the “Download Selected” control to be renamed.
- [var downloadAllControlLabel: String!](./downloadallcontrollabel.md)
  Allows the “Download All” control to be renamed.
- [var displaysDownloadsDirectoryControl: Bool](./displaysdownloadsdirectorycontrol.md)
  Specifies whether the downloads directory control should be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikcameradeviceview/downloadsdirectory)*