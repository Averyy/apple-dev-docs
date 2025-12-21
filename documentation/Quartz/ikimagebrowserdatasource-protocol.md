# IKImageBrowserDataSource Protocol

**Framework**: Quartz

The `IKImageBrowserDataSource` informal protocol declares the methods that an instance of the [`IKImageBrowserView`](ikimagebrowserview.md)  class uses to access the contents of its data source object.

## Topics

### Providing Information About Items (Required)
- [func numberOfItems(inImageBrowser: IKImageBrowserView!) -> Int](../ObjectiveC/NSObject-swift.class/numberOfItems(inImageBrowser:).md)
  Returns the number of records managed by the data source object.
- [func imageBrowser(IKImageBrowserView!, itemAt: Int) -> Any!](../ObjectiveC/NSObject-swift.class/imageBrowser(_:itemAt:).md)
  Returns an object for the item in an image browser view that corresponds to the specified index.
### Supporting Item Editing (Optional)
- [func imageBrowser(IKImageBrowserView!, removeItemsAt: IndexSet!)](../ObjectiveC/NSObject-swift.class/imageBrowser(_:removeItemsAt:).md)
  Signals that a remove operation should be applied to the specified items.
- [func imageBrowser(IKImageBrowserView!, moveItemsAt: IndexSet!, to: Int) -> Bool](../ObjectiveC/NSObject-swift.class/imageBrowser(_:moveItemsAt:to:).md)
  Signals that the specified items should be moved to the specified destination.
- [func imageBrowser(IKImageBrowserView!, writeItemsAt: IndexSet!, to: NSPasteboard!) -> Int](../ObjectiveC/NSObject-swift.class/imageBrowser(_:writeItemsAt:to:).md)
  Signals that a drag should begin.
### Providing Information About Groups (Optional)
- [func numberOfGroups(inImageBrowser: IKImageBrowserView!) -> Int](../ObjectiveC/NSObject-swift.class/numberOfGroups(inImageBrowser:).md)
  Returns the number of groups in an image browser view.
- [func imageBrowser(IKImageBrowserView!, groupAt: Int) -> [AnyHashable : Any]!](../ObjectiveC/NSObject-swift.class/imageBrowser(_:groupAt:).md)
  Returns the group at the specified index.

## See Also

- [protocol IKCameraDeviceViewDelegate](ikcameradeviceviewdelegate.md)
  The `IKCameraDeviceViewDelegate` protocol is adopted by the delegate of the [`IKCameraDeviceView`](ikcameradeviceview.md) class. It allows downloading of camera content, handling selection changes, and handling errors.
- [protocol IKDeviceBrowserViewDelegate](ikdevicebrowserviewdelegate.md)
  The `IKDeviceBrowserViewDelegate` defines the methods that the delegate of the [`IKDeviceBrowserView`](ikdevicebrowserview.md) class can implement. All the methods are optional.
- [protocol IKFilterCustomUIProvider](ikfiltercustomuiprovider.md)
  A protocol used to provide a custom UI.
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

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserdatasource-protocol)*