# IKFilterCustomUIProvider

**Framework**: Quartz  
**Kind**: protocol

A protocol used to provide a custom UI.

**Availability**:
- macOS 10.4+

## Declaration

```swift
protocol IKFilterCustomUIProvider
```

#### Overview

The `IKFilterCustomUIProvider` protocol is an addition to the [`CIFilter`](https://developer.apple.com/documentation/coreimage/cifilter) class that defines a method for providing a view for a filter. This protocol is implemented by any filter that provides its own user interface.

## Topics

### Providing a Custom View
- [func provideView(forUIConfiguration: [AnyHashable : Any]!, excludedKeys: [Any]!) -> IKFilterUIView!](ikfiltercustomuiprovider/provideview(foruiconfiguration:excludedkeys:).md)
  Provides a custom view for a filter.

## See Also

- [protocol IKCameraDeviceViewDelegate](ikcameradeviceviewdelegate.md)
  The `IKCameraDeviceViewDelegate` protocol is adopted by the delegate of the [`IKCameraDeviceView`](ikcameradeviceview.md) class. It allows downloading of camera content, handling selection changes, and handling errors.
- [protocol IKDeviceBrowserViewDelegate](ikdevicebrowserviewdelegate.md)
  The `IKDeviceBrowserViewDelegate` defines the methods that the delegate of the [`IKDeviceBrowserView`](ikdevicebrowserview.md) class can implement. All the methods are optional.
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

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikfiltercustomuiprovider)*