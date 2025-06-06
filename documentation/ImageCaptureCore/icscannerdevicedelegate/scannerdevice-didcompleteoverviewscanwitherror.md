# scannerDevice(_:didCompleteOverviewScanWithError:)

**Framework**: ImageCaptureCore  
**Kind**: method

Tells the client when the scanner completes an overview scan.

**Availability**:
- macOS 10.4+

## Declaration

```swift
optional func scannerDevice(_ scanner: ICScannerDevice, didCompleteOverviewScanWithError error: (any Error)?)
```

## See Also

- [func scannerDevice(ICScannerDevice, didCompleteScanWithError: (any Error)?)](icscannerdevicedelegate/scannerdevice(_:didcompletescanwitherror:).md)
  Tells the client when the scanner completes a scan.
- [func scannerDevice(ICScannerDevice, didScanTo: ICScannerBandData)](icscannerdevicedelegate/scannerdevice(_:didscanto:)-6tht3.md)
  Tells the client when the scanner receives the requested scan progress notification and a band of data is sent for each notification received.
- [func scannerDevice(ICScannerDevice, didScanTo: URL)](icscannerdevicedelegate/scannerdevice(_:didscanto:)-10whl.md)
  Tells the client when the scanner receives the requested scan.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icscannerdevicedelegate/scannerdevice(_:didcompleteoverviewscanwitherror:))*