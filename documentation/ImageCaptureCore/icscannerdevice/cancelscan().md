# cancelScan()

**Framework**: ImageCaptureCore  
**Kind**: method  
**Role**: Instance Method

Cancels the current scan.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func cancelScan()
```

```objc
- (void) cancelScan;
```

## Discussion

Cancels the scan in progress by calling [`requestOverviewScan()`](./requestoverviewscan%28%29.md) or [`requestScan()`](./requestscan%28%29.md).

## See Also

### Performing a Scan
- [func requestOpenSession(withCredentials: String, password: String)](./requestopensession%28withcredentials,password%29.md)
  Opens a session on the protected device with the authorized username and passcode.
- [func requestOverviewScan()](./requestoverviewscan%28%29.md)
  Starts an overview scan on the selected functional unit.
- [func requestScan()](./requestscan%28%29.md)
  Starts a scan on the selected functional unit.
- [var documentName: String](./documentname.md)
  The document’s name.
- [var documentUTI: String](./documentuti.md)
  The document’s uniform type identifier.
- [var downloadsDirectory: URL](./downloadsdirectory.md)
  The downloads directory.
- [var transferMode: ICScannerTransferMode](./transfermode.md)
  The transfer mode for the scanned document.
- [var maxMemoryBandSize: UInt32](./maxmemorybandsize.md)
  The total maximum band size requested when performing a memory-based transfer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icscannerdevice/cancelscan())*