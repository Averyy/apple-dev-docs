# IKImageBrowserItem Protocol

**Framework**: Quartz

The `IKImageBrowserItem` informal protocol declares the methods that an instance of the [`IKImageBrowserView`](ikimagebrowserview.md) class uses to access the contents of its data source for a given item. Some of the methods in this protocol are needed frequently, so you should implement them efficiently.

## Topics

### Providing Required Information for an Image
- [func imageUID() -> String!](../ObjectiveC/NSObject-swift.class/imageUID.md)
  Returns a unique string that identifies the data source item.
- [func imageRepresentationType() -> String!](../ObjectiveC/NSObject-swift.class/imageRepresentationType.md)
  Returns the representation type of the image to display.
- [func imageRepresentation() -> Any!](../ObjectiveC/NSObject-swift.class/imageRepresentation.md)
  Returns the image to display.
### Providing Optional Information for an Image
- [func imageVersion() -> Int](../ObjectiveC/NSObject-swift.class/imageVersion.md)
  Returns the version of the item.
- [func imageTitle() -> String!](../ObjectiveC/NSObject-swift.class/imageTitle.md)
  Returns the display title of the image.
- [func imageSubtitle() -> String!](../ObjectiveC/NSObject-swift.class/imageSubtitle.md)
  Returns the display subtitle of the image.
### Constants
- [Image Representation Types](image-representation-types.md)
  Representation types for images.

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
- [protocol IKImageEditPanelDataSource](ikimageeditpaneldatasource.md)
  The `IKImageEditPanelDataSource` protocol describes the methods that an [`IKImageEditPanel`](ikimageeditpanel.md) object uses to access the contents of its data source object.
- [protocol IKScannerDeviceViewDelegate](ikscannerdeviceviewdelegate.md)
  The `IKScannerDeviceViewDelegate` protocol defines the delegate protocol that the [`IKScannerDeviceView`](ikscannerdeviceview.md) delegate must conform to.
- [protocol IKSlideshowDataSource](ikslideshowdatasource.md)
  The `IKSlideshowDataSource` protocol describes the methods that an [`IKSlideshow`](ikslideshow.md) object uses to access the contents of its data source object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowseritem-protocol)*