# IKImageBrowserDelegate Protocol

**Framework**: Quartz

The `IKImageBrowserDelegate` is an informal protocol for the delegate of an [`IKImageBrowserView`](ikimagebrowserview.md) object. You can implement these methods to perform custom tasks when in response to events in the image browser view.

## Topics

### Performing Custom Tasks in Response to User Events
- [func imageBrowser(_ aBrowser: IKImageBrowserView!, backgroundWasRightClickedWith event: NSEvent!)](../ObjectiveC/NSObject-swift.class/imageBrowser(_:backgroundWasRightClickedWith:).md)
  Performs custom tasks when the user right-clicks the image browser view background.
- [func imageBrowser(_ aBrowser: IKImageBrowserView!, cellWasRightClickedAt index: Int, with event: NSEvent!)](../ObjectiveC/NSObject-swift.class/imageBrowser(_:cellWasRightClickedAt:with:).md)
  Performs custom tasks when the user right-clicks an item in the image browser view.
- [func imageBrowser(_ aBrowser: IKImageBrowserView!, cellWasDoubleClickedAt index: Int)](../ObjectiveC/NSObject-swift.class/imageBrowser(_:cellWasDoubleClickedAt:).md)
  Performs custom tasks when the user double-clicks an item in the image browser view.
- [func imageBrowserSelectionDidChange(_ aBrowser: IKImageBrowserView!)](../ObjectiveC/NSObject-swift.class/imageBrowserSelectionDidChange(_:).md)
  Performs custom tasks when the selection changes.

## See Also

- [protocol IKCameraDeviceViewDelegate](ikcameradeviceviewdelegate.md)
  The `IKCameraDeviceViewDelegate` protocol is adopted by the delegate of the [`IKCameraDeviceView`](ikcameradeviceview.md) class. It allows downloading of camera content, handling selection changes, and handling errors.
- [protocol IKDeviceBrowserViewDelegate](ikdevicebrowserviewdelegate.md)
  The `IKDeviceBrowserViewDelegate` defines the methods that the delegate of the [`IKDeviceBrowserView`](ikdevicebrowserview.md) class can implement. All the methods are optional.
- [protocol IKFilterCustomUIProvider](ikfiltercustomuiprovider.md)
  A protocol used to provide a custom UI.
- [IKImageBrowserDataSource Protocol](ikimagebrowserdatasource-protocol.md)
  The `IKImageBrowserDataSource` informal protocol declares the methods that an instance of the [`IKImageBrowserView`](ikimagebrowserview.md)  class uses to access the contents of its data source object.
- [IKImageBrowserItem Protocol](ikimagebrowseritem-protocol.md)
  The `IKImageBrowserItem` informal protocol declares the methods that an instance of the [`IKImageBrowserView`](ikimagebrowserview.md) class uses to access the contents of its data source for a given item. Some of the methods in this protocol are needed frequently, so you should implement them efficiently.
- [protocol IKImageEditPanelDataSource](ikimageeditpaneldatasource.md)
  The `IKImageEditPanelDataSource` protocol describes the methods that an [`IKImageEditPanel`](ikimageeditpanel.md) object uses to access the contents of its data source object.
- [protocol IKScannerDeviceViewDelegate](ikscannerdeviceviewdelegate.md)
  The `IKScannerDeviceViewDelegate` protocol defines the delegate protocol that the [`IKScannerDeviceView`](ikscannerdeviceview.md) delegate must conform to.
- [protocol IKSlideshowDataSource](ikslideshowdatasource.md)
  The `IKSlideshowDataSource` protocol describes the methods that an [`IKSlideshow`](ikslideshow.md) object uses to access the contents of its data source object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserdelegate-protocol)*