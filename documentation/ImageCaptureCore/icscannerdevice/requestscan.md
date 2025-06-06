# requestScan()

**Framework**: ImageCaptureCore  
**Kind**: method

Starts a scan on the selected functional unit.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func requestScan()
```

#### Discussion

Once the request to start an overview scan has completed, [`scannerDevice(_:didCompleteScanWithError:)`](icscannerdevicedelegate/scannerdevice(_:didcompletescanwitherror:).md) is called on the delegate.

## See Also

- [func requestOpenSession(withCredentials: String, password: String)](icscannerdevice/requestopensession(withcredentials:password:).md)
  Opens a session on the protected device with the authorized username and passcode.
- [func requestOverviewScan()](icscannerdevice/requestoverviewscan.md)
  Starts an overview scan on the selected functional unit.
- [func cancelScan()](icscannerdevice/cancelscan.md)
  Cancels the current scan.
- [var documentName: String](icscannerdevice/documentname.md)
  The document’s name.
- [var documentUTI: String](icscannerdevice/documentuti.md)
  The document’s uniform type identifier.
- [var downloadsDirectory: URL](icscannerdevice/downloadsdirectory.md)
  The downloads directory.
- [var transferMode: ICScannerTransferMode](icscannerdevice/transfermode.md)
  The transfer mode for the scanned document.
- [var maxMemoryBandSize: UInt32](icscannerdevice/maxmemorybandsize.md)
  The total maximum band size requested when performing a memory-based transfer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icscannerdevice/requestscan())*