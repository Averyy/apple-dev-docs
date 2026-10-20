# transferMode

**Framework**: Quartz  
**Kind**: property  
**Role**: Instance Property

Determines how the scanned content is provided to the delegate.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var transferMode: IKScannerDeviceViewTransferMode { get set }
```

```objc
@property IKScannerDeviceViewTransferMode transferMode;
```

#### Discussion

The supported constants are defined in [`IKScannerDeviceViewTransferMode`](../ikscannerdeviceviewtransfermode.md).

## See Also

### Configuring Downloading
- [var displaysDownloadsDirectoryControl: Bool](./displaysdownloadsdirectorycontrol.md)
  Determines whether the downloads directory control is displayed.
- [var downloadsDirectory: URL!](./downloadsdirectory.md)
  The directory where scans are saved.
- [var documentName: String!](./documentname.md)
  Returns the document name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikscannerdeviceview/transfermode)*