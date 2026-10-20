# downloadsDirectory

**Framework**: ImageCaptureCore  
**Kind**: property  
**Role**: Instance Property

The downloads directory.

**Availability**:
- macOS 10.4+

## Declaration

```swift
var downloadsDirectory: URL { get set }
```

```objc
@property (retain) NSURL * downloadsDirectory;
```

## See Also

### Performing a Scan
- [func requestOpenSession(withCredentials: String, password: String)](./requestopensession%28withcredentials,password%29.md)
  Opens a session on the protected device with the authorized username and passcode.
- [func requestOverviewScan()](./requestoverviewscan%28%29.md)
  Starts an overview scan on the selected functional unit.
- [func requestScan()](./requestscan%28%29.md)
  Starts a scan on the selected functional unit.
- [func cancelScan()](./cancelscan%28%29.md)
  Cancels the current scan.
- [var documentName: String](./documentname.md)
  The document’s name.
- [var documentUTI: String](./documentuti.md)
  The document’s uniform type identifier.
- [var transferMode: ICScannerTransferMode](./transfermode.md)
  The transfer mode for the scanned document.
- [var maxMemoryBandSize: UInt32](./maxmemorybandsize.md)
  The total maximum band size requested when performing a memory-based transfer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icscannerdevice/downloadsdirectory)*