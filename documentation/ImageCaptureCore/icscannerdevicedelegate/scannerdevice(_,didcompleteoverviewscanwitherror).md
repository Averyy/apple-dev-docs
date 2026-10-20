# scannerDevice(_:didCompleteOverviewScanWithError:)

**Framework**: ImageCaptureCore  
**Kind**: method  
**Role**: Instance Method

Tells the client when the scanner completes an overview scan.

**Availability**:
- macOS 10.4+

## Declaration

```swift
optional func scannerDevice(_ scanner: ICScannerDevice, didCompleteOverviewScanWithError error: (any Error)?)
```

```objc
- (void) scannerDevice:(ICScannerDevice *) scanner didCompleteOverviewScanWithError:(NSError *) error;
```

## See Also

### Performing a Scan
- [func scannerDevice(ICScannerDevice, didCompleteScanWithError: (any Error)?)](./scannerdevice%28_,didcompletescanwitherror%29.md)
  Tells the client when the scanner completes a scan.
- [func scannerDevice(ICScannerDevice, didScanTo: ICScannerBandData)](./scannerdevice%28_,didscanto%29-6tht3.md)
  Tells the client when the scanner receives the requested scan progress notification and a band of data is sent for each notification received.
- [func scannerDevice(ICScannerDevice, didScanTo: URL)](./scannerdevice%28_,didscanto%29-10whl.md)
  Tells the client when the scanner receives the requested scan.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icscannerdevicedelegate/scannerdevice(_:didcompleteoverviewscanwitherror:))*