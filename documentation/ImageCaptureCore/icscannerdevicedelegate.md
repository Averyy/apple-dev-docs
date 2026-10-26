# ICScannerDeviceDelegate

**Framework**: ImageCaptureCore  
**Kind**: protocol  
**Role**: Protocol

Methods for determining availability, selecting a functional unit, and performing scans on connected scanners.

**Availability**:
- macOS 10.4+

## Declaration

```swift
protocol ICScannerDeviceDelegate : ICDeviceDelegate
```

```objc
@protocol ICScannerDeviceDelegate <ICDeviceDelegate>
```

## Topics

### Determining Scanner Availability
- [func scannerDeviceDidBecomeAvailable(ICScannerDevice)](./icscannerdevicedelegate/scannerdevicedidbecomeavailable%28_%29.md)
  Tells the client when another client closes the current open session on the scanner.
### Selecting a Functional Unit
- [func scannerDevice(ICScannerDevice, didSelect: ICScannerFunctionalUnit, error: (any Error)?)](./icscannerdevicedelegate/scannerdevice%28_,didselect,error%29.md)
  Tells the client when a functional unit is selected on the scanner.
### Performing a Scan
- [func scannerDevice(ICScannerDevice, didCompleteOverviewScanWithError: (any Error)?)](./icscannerdevicedelegate/scannerdevice%28_,didcompleteoverviewscanwitherror%29.md)
  Tells the client when the scanner completes an overview scan.
- [func scannerDevice(ICScannerDevice, didCompleteScanWithError: (any Error)?)](./icscannerdevicedelegate/scannerdevice%28_,didcompletescanwitherror%29.md)
  Tells the client when the scanner completes a scan.
- [func scannerDevice(ICScannerDevice, didScanTo: ICScannerBandData)](./icscannerdevicedelegate/scannerdevice%28_,didscanto%29-6tht3.md)
  Tells the client when the scanner receives the requested scan progress notification and a band of data is sent for each notification received.
- [func scannerDevice(ICScannerDevice, didScanTo: URL)](./icscannerdevicedelegate/scannerdevice%28_,didscanto%29-10whl.md)
  Tells the client when the scanner receives the requested scan.
### Deprecated
- [- scannerDevice:didScanToURL:data:](./icscannerdevicedelegate/scannerdevice_didscantourl_data_.md)
  Tells the client when the scanner device receives the requested scan.

## Relationships

### Inherits From
- [ICDeviceDelegate](./icdevicedelegate.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Scanners
- [class ICScannerDevice](./icscannerdevice.md)
  An object that represents a scanner.
- [Scanner Configuration](./scanner-configuration.md)
  Examine a scanner’s functional units and features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icscannerdevicedelegate)*