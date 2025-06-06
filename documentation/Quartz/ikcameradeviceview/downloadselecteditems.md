# downloadSelectedItems(_:)

**Framework**: Quartz  
**Kind**: method

Deletes the selected items from the camera.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@IBAction
@MainActor func downloadSelectedItems(_ sender: Any!)
```

#### Discussion

This method is can be connected to a user interface item in Interface Builder.

## Parameters

- `sender`: The object that sent the message.

## See Also

- [var canDownloadSelectedItems: Bool](ikcameradeviceview/candownloadselecteditems.md)
  Returns whether the selected items can be downloaded
- [var downloadsDirectory: URL!](ikcameradeviceview/downloadsdirectory.md)
  Specifies the directory where files are downloaded
- [func downloadAllItems(Any!)](ikcameradeviceview/downloadallitems(_:).md)
  Downloads all the items.
- [var downloadSelectedControlLabel: String!](ikcameradeviceview/downloadselectedcontrollabel.md)
  Allows the “Download Selected” control to be renamed.
- [var downloadAllControlLabel: String!](ikcameradeviceview/downloadallcontrollabel.md)
  Allows the “Download All” control to be renamed.
- [var displaysDownloadsDirectoryControl: Bool](ikcameradeviceview/displaysdownloadsdirectorycontrol.md)
  Specifies whether the downloads directory control should be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikcameradeviceview/downloadselecteditems(_:))*