# requestOpenSession(withCredentials:password:)

**Framework**: ImageCaptureCore  
**Kind**: method  
**Role**: Instance Method

Opens a session on the protected device with the authorized username and passcode.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func requestOpenSession(withCredentials username: String, password: String)
```

```objc
- (void) requestOpenSessionWithCredentials:(NSString *) username password:(NSString *) password;
```

## Discussion

If the device reports a failure of credentials, you can provide them here for the launch. A client must open a session on a device in order to use the device.

Before calling this method, set the receiver’s delegate; otherwise, the request is ignored.

Once the request to open the session has completed, [`device(_:didOpenSessionWithError:)`](../icdevicedelegate/device%28_,didopensessionwitherror%29.md) is called on the delegate.

No more messages are sent to the delegate if this request fails.

## See Also

### Performing a Scan
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
- [var downloadsDirectory: URL](./downloadsdirectory.md)
  The downloads directory.
- [var transferMode: ICScannerTransferMode](./transfermode.md)
  The transfer mode for the scanned document.
- [var maxMemoryBandSize: UInt32](./maxmemorybandsize.md)
  The total maximum band size requested when performing a memory-based transfer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icscannerdevice/requestopensession(withcredentials:password:))*