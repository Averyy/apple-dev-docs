# scannerDevice(_:didCompleteScanWithError:)

**Framework**: ImageCaptureCore  
**Kind**: method  
**Role**: Instance Method

Tells the client when the scanner completes a scan.

**Availability**:
- macOS 10.4+

## Declaration

```swift
optional func scannerDevice(_ scanner: ICScannerDevice, didCompleteScanWithError error: (any Error)?)
```

```objc
- (void) scannerDevice:(ICScannerDevice *) scanner didCompleteScanWithError:(NSError *) error;
```

## See Also

### Performing a Scan
- [func scannerDevice(ICScannerDevice, didCompleteOverviewScanWithError: (any Error)?)](./scannerdevice%28_,didcompleteoverviewscanwitherror%29.md)
  Tells the client when the scanner completes an overview scan.
- [func scannerDevice(ICScannerDevice, didScanTo: ICScannerBandData)](./scannerdevice%28_,didscanto%29-6tht3.md)
  Tells the client when the scanner receives the requested scan progress notification and a band of data is sent for each notification received.
- [func scannerDevice(ICScannerDevice, didScanTo: URL)](./scannerdevice%28_,didscanto%29-10whl.md)
  Tells the client when the scanner receives the requested scan.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icscannerdevicedelegate/scannerdevice(_:didcompletescanwitherror:))*