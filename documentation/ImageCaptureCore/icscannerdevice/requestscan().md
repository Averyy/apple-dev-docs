# requestScan()

**Framework**: ImageCaptureCore  
**Kind**: method  
**Role**: Instance Method

Starts a scan on the selected functional unit.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func requestScan()
```

```objc
- (void) requestScan;
```

#### Discussion

Once the request to start an overview scan has completed, [`scannerDevice(_:didCompleteScanWithError:)`](../icscannerdevicedelegate/scannerdevice%28_,didcompletescanwitherror%29.md) is called on the delegate.

## See Also

### Performing a Scan
- [func requestOpenSession(withCredentials: String, password: String)](./requestopensession%28withcredentials,password%29.md)
  Opens a session on the protected device with the authorized username and passcode.
- [func requestOverviewScan()](./requestoverviewscan%28%29.md)
  Starts an overview scan on the selected functional unit.
- [func cancelScan()](./cancelscan%28%29.md)
  Cancels the current scan.
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

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icscannerdevice/requestscan())*