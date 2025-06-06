# maxMemoryBandSize

**Framework**: ImageCaptureCore  
**Kind**: property

The total maximum band size requested when performing a memory-based transfer.

**Availability**:
- macOS 10.4+

## Declaration

```swift
var maxMemoryBandSize: UInt32 { get set }
```

## See Also

- [func requestOpenSession(withCredentials: String, password: String)](icscannerdevice/requestopensession(withcredentials:password:).md)
  Opens a session on the protected device with the authorized username and passcode.
- [func requestOverviewScan()](icscannerdevice/requestoverviewscan.md)
  Starts an overview scan on the selected functional unit.
- [func requestScan()](icscannerdevice/requestscan.md)
  Starts a scan on the selected functional unit.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icscannerdevice/maxmemorybandsize)*