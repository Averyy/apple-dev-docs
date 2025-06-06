# IKCameraDeviceViewDelegate

**Framework**: Quartz  
**Kind**: protocol

The `IKCameraDeviceViewDelegate` protocol is adopted by the delegate of the [`IKCameraDeviceView`](ikcameradeviceview.md) class. It allows downloading of camera content, handling selection changes, and handling errors.

**Availability**:
- macOS 10.4+

## Declaration

```swift
protocol IKCameraDeviceViewDelegate
```

## Topics

### Downloading Camera Content
- [func cameraDeviceView(IKCameraDeviceView!, didDownloadFile: ICCameraFile!, location: URL!, fileData: Data!, error: (any Error)!)](ikcameradeviceviewdelegate/cameradeviceview(_:diddownloadfile:location:filedata:error:).md)
  Invoked for each file that is downloaded from the camera device.
### Detecting Selection Changes
- [func cameraDeviceViewSelectionDidChange(IKCameraDeviceView!)](ikcameradeviceviewdelegate/cameradeviceviewselectiondidchange(_:).md)
  Invoked when the selection changed.
### Managing Errors
- [func cameraDeviceView(IKCameraDeviceView!, didEncounterError: (any Error)!)](ikcameradeviceviewdelegate/cameradeviceview(_:didencountererror:).md)
  Invoked when the camera encounters an error.

## See Also

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
- [protocol IKScannerDeviceViewDelegate](ikscannerdeviceviewdelegate.md)
  The `IKScannerDeviceViewDelegate` protocol defines the delegate protocol that the [`IKScannerDeviceView`](ikscannerdeviceview.md) delegate must conform to.
- [protocol IKSlideshowDataSource](ikslideshowdatasource.md)
  The `IKSlideshowDataSource` protocol describes the methods that an [`IKSlideshow`](ikslideshow.md) object uses to access the contents of its data source object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikcameradeviceviewdelegate)*