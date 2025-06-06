# IKScannerDeviceViewDelegate

**Framework**: Quartz  
**Kind**: protocol

The `IKScannerDeviceViewDelegate` protocol defines the delegate protocol that the [`IKScannerDeviceView`](ikscannerdeviceview.md) delegate must conform to.

**Availability**:
- macOS 10.4+

## Declaration

```swift
protocol IKScannerDeviceViewDelegate
```

## Topics

### Scan Completed
- [func scannerDeviceView(IKScannerDeviceView!, didScanTo: URL!, fileData: Data!, error: (any Error)!)](ikscannerdeviceviewdelegate/scannerdeviceview(_:didscanto:filedata:error:).md)
  Invoked when the scan has completed and the data is available.
### Scanner Encountered Error
- [func scannerDeviceView(IKScannerDeviceView!, didEncounterError: (any Error)!)](ikscannerdeviceviewdelegate/scannerdeviceview(_:didencountererror:).md)
  Invoked whenever the scanner encounters an error.
### Instance Methods
- [func scannerDeviceView(IKScannerDeviceView!, didScanTo: URL!, error: (any Error)!)](ikscannerdeviceviewdelegate/scannerdeviceview(_:didscanto:error:).md)
- [func scannerDeviceView(IKScannerDeviceView!, didScanTo: ICScannerBandData!, scanInfo: [AnyHashable : Any]!, error: (any Error)!)](ikscannerdeviceviewdelegate/scannerdeviceview(_:didscanto:scaninfo:error:).md)

## See Also

- [protocol IKCameraDeviceViewDelegate](ikcameradeviceviewdelegate.md)
  The `IKCameraDeviceViewDelegate` protocol is adopted by the delegate of the [`IKCameraDeviceView`](ikcameradeviceview.md) class. It allows downloading of camera content, handling selection changes, and handling errors.
- [protocol IKDeviceBrowserViewDelegate](ikdevicebrowserviewdelegate.md)
  The `IKDeviceBrowserViewDelegate` defines the methods that the delegate of the [`IKDeviceBrowserView`](ikdevicebrowserview.md) class can implement. All the methods are optional.
- [protocol IKFilterCustomUIProvider](ikfiltercustomuiprovider.md)
  A protocol used to provide a custom UI.
- [IKImageBrowserDataSource Protocol](ikimagebrowserdatasource-protocol.md)
  The `IKImageBrowserDataSource` informal protocol declares the methods that an instance of the [`IKImageBrowserView`](ikimagebrowserview.md)  class uses to access the contents of its data source object.
- [IKImageBrowserDelegate Protocol](ikimagebrowserdelegate-protocol.md)
  The `IKImageBrowserDelegate` is an informal protocol for the delegate of an [`IKImageBrowserView`](ikimagebrowserview.md) object. You can implement these methods to perform custom tasks when in response to events in the image browser view.
- [IKImageBrowserItem Protocol](ikimagebrowseritem-protocol.md)
  The `IKImageBrowserItem` informal protocol declares the methods that an instance of the [`IKImageBrowserView`](ikimagebrowserview.md) class uses to access the contents of its data source for a given item. Some of the methods in this protocol are needed frequently, so you should implement them efficiently.
- [protocol IKImageEditPanelDataSource](ikimageeditpaneldatasource.md)
  The `IKImageEditPanelDataSource` protocol describes the methods that an [`IKImageEditPanel`](ikimageeditpanel.md) object uses to access the contents of its data source object.
- [protocol IKSlideshowDataSource](ikslideshowdatasource.md)
  The `IKSlideshowDataSource` protocol describes the methods that an [`IKSlideshow`](ikslideshow.md) object uses to access the contents of its data source object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikscannerdeviceviewdelegate)*