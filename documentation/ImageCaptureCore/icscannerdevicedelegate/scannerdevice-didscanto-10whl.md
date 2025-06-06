# scannerDevice(_:didScanTo:)

**Framework**: ImageCaptureCore  
**Kind**: method

Tells the client when the scanner receives the requested scan.

**Availability**:
- macOS 10.7+

## Declaration

```swift
optional func scannerDevice(_ scanner: ICScannerDevice, didScanTo url: URL)
```

#### Discussion

If the [`selectedFunctionalUnit`](icscannerdevice/selectedfunctionalunit.md) is a document feeder, then this message is sent once for each scanned page.

## See Also

- [func scannerDevice(ICScannerDevice, didCompleteOverviewScanWithError: (any Error)?)](icscannerdevicedelegate/scannerdevice(_:didcompleteoverviewscanwitherror:).md)
  Tells the client when the scanner completes an overview scan.
- [func scannerDevice(ICScannerDevice, didCompleteScanWithError: (any Error)?)](icscannerdevicedelegate/scannerdevice(_:didcompletescanwitherror:).md)
  Tells the client when the scanner completes a scan.
- [func scannerDevice(ICScannerDevice, didScanTo: ICScannerBandData)](icscannerdevicedelegate/scannerdevice(_:didscanto:)-6tht3.md)
  Tells the client when the scanner receives the requested scan progress notification and a band of data is sent for each notification received.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icscannerdevicedelegate/scannerdevice(_:didscanto:)-10whl)*