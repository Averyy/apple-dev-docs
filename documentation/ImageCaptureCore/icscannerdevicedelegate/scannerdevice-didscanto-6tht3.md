# scannerDevice(_:didScanTo:)

**Framework**: ImageCaptureCore  
**Kind**: method

Tells the client when the scanner receives the requested scan progress notification and a band of data is sent for each notification received.

**Availability**:
- macOS 10.7+

## Declaration

```swift
optional func scannerDevice(_ scanner: ICScannerDevice, didScanTo data: ICScannerBandData)
```

#### Discussion

In memory transfer mode, this method sends a band of the size selected by the client using the [`maxMemoryBandSize`](icscannerdevice/maxmemorybandsize.md) property.

## See Also

- [func scannerDevice(ICScannerDevice, didCompleteOverviewScanWithError: (any Error)?)](icscannerdevicedelegate/scannerdevice(_:didcompleteoverviewscanwitherror:).md)
  Tells the client when the scanner completes an overview scan.
- [func scannerDevice(ICScannerDevice, didCompleteScanWithError: (any Error)?)](icscannerdevicedelegate/scannerdevice(_:didcompletescanwitherror:).md)
  Tells the client when the scanner completes a scan.
- [func scannerDevice(ICScannerDevice, didScanTo: URL)](icscannerdevicedelegate/scannerdevice(_:didscanto:)-10whl.md)
  Tells the client when the scanner receives the requested scan.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icscannerdevicedelegate/scannerdevice(_:didscanto:)-6tht3)*