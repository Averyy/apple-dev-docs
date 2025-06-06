# IKImageEditPanelDataSource

**Framework**: Quartz  
**Kind**: protocol

The `IKImageEditPanelDataSource` protocol describes the methods that an [`IKImageEditPanel`](ikimageeditpanel.md) object uses to access the contents of its data source object.

**Availability**:
- macOS 10.4+

## Declaration

```swift
protocol IKImageEditPanelDataSource
```

## Topics

### Getting and Setting Image Properties
- [var imageProperties: [AnyHashable : Any]!](ikimageeditpaneldatasource/imageproperties.md)
  Returns a dictionary of the image properties associated with the image in the image edit panel.
- [func setImage(CGImage!, imageProperties: [AnyHashable : Any]!)](ikimageeditpaneldatasource/setimage(_:imageproperties:).md)
  Sets an image with the specified properties.
### Getting Images From the Data Source
- [var image: CGImage!](ikimageeditpaneldatasource/image.md)
  Returns an image.
- [func thumbnail(withMaximumSize: NSSize) -> Unmanaged<CGImage>!](ikimageeditpaneldatasource/thumbnail(withmaximumsize:).md)
  Returns a thumbnail image whose size is no larger than the specified size.
### New Methods
- [var hasAdjustMode: Bool](ikimageeditpaneldatasource/hasadjustmode.md)
  Returns whether the adjust mode view tab should be displayed.
- [var hasDetailsMode: Bool](ikimageeditpaneldatasource/hasdetailsmode.md)
  Returns whether the details mode view tab should be displayed.
- [var hasEffectsMode: Bool](ikimageeditpaneldatasource/haseffectsmode.md)
  Returns whether the effects mode view tab should be displayed.

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
- [protocol IKScannerDeviceViewDelegate](ikscannerdeviceviewdelegate.md)
  The `IKScannerDeviceViewDelegate` protocol defines the delegate protocol that the [`IKScannerDeviceView`](ikscannerdeviceview.md) delegate must conform to.
- [protocol IKSlideshowDataSource](ikslideshowdatasource.md)
  The `IKSlideshowDataSource` protocol describes the methods that an [`IKSlideshow`](ikslideshow.md) object uses to access the contents of its data source object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimageeditpaneldatasource)*