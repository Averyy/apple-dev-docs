# downloadAllItems(_:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Downloads all the items.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@IBAction
func downloadAllItems(_ sender: Any!)
```

```objc
- (void) downloadAllItems:(id) sender;
```

#### Discussion

This method is can be connected to a user interface item in Interface Builder.

## Parameters

- `sender`: The object that sent the message.

## See Also

### Configuring Download Interface and Downloading Files
- [var canDownloadSelectedItems: Bool](./candownloadselecteditems.md)
  Returns whether the selected items can be downloaded
- [var downloadsDirectory: URL!](./downloadsdirectory.md)
  Specifies the directory where files are downloaded
- [func downloadSelectedItems(Any!)](./downloadselecteditems%28_%29.md)
  Deletes the selected items from the camera.
- [var downloadSelectedControlLabel: String!](./downloadselectedcontrollabel.md)
  Allows the “Download Selected” control to be renamed.
- [var downloadAllControlLabel: String!](./downloadallcontrollabel.md)
  Allows the “Download All” control to be renamed.
- [var displaysDownloadsDirectoryControl: Bool](./displaysdownloadsdirectorycontrol.md)
  Specifies whether the downloads directory control should be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikcameradeviceview/downloadallitems(_:))*