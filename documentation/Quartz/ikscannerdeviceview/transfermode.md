# transferMode

**Framework**: Quartz  
**Kind**: property

Determines how the scanned content is provided to the delegate.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
var transferMode: IKScannerDeviceViewTransferMode { get set }
```

#### Discussion

The supported constants are defined in [`IKScannerDeviceViewTransferMode`](ikscannerdeviceviewtransfermode.md).

## See Also

- [var displaysDownloadsDirectoryControl: Bool](ikscannerdeviceview/displaysdownloadsdirectorycontrol.md)
  Determines whether the downloads directory control is displayed.
- [var downloadsDirectory: URL!](ikscannerdeviceview/downloadsdirectory.md)
  The directory where scans are saved.
- [var documentName: String!](ikscannerdeviceview/documentname.md)
  Returns the document name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikscannerdeviceview/transfermode)*