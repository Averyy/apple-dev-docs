# IKSlideshowDataSource

**Framework**: Quartz  
**Kind**: protocol  
**Role**: Protocol

The `IKSlideshowDataSource` protocol describes the methods that an [`IKSlideshow`](./ikslideshow.md) object uses to access the contents of its data source object.

**Availability**:
- macOS 10.4+

## Declaration

```swift
protocol IKSlideshowDataSource
```

```objc
@protocol IKSlideshowDataSource
```

#### Overview

> ❗ **Important**:  Slide show data source methods may be called on secondary threads. When you implement these methods, you must ensure that they are safe to run on threads other than the main thread.

## Topics

### Providing Slideshow Information
- [func numberOfSlideshowItems() -> Int](./ikslideshowdatasource/numberofslideshowitems%28%29.md)
  Returns the number of items in a slideshow.
- [func slideshowItem(at: Int) -> Any!](./ikslideshowdatasource/slideshowitem%28at%29.md)
  Returns the item for a given index
- [func nameOfSlideshowItem(at: Int) -> String!](./ikslideshowdatasource/nameofslideshowitem%28at%29.md)
  Returns the display name for item at the specified index.
- [func canExportSlideshowItem(at: Int, toApplication: String!) -> Bool](./ikslideshowdatasource/canexportslideshowitem%28at,toapplication%29.md)
  Reports whether the export button should be enabled for a slideshow item.
### Performing Custom Tasks
- [func slideshowWillStart()](./ikslideshowdatasource/slideshowwillstart%28%29.md)
  Performs custom tasks when the slideshow is about to start.
- [func slideshowDidStop()](./ikslideshowdatasource/slideshowdidstop%28%29.md)
  Performs custom tasks when the slideshow stops.
- [func slideshowDidChangeCurrentIndex(Int)](./ikslideshowdatasource/slideshowdidchangecurrentindex%28_%29.md)
  Performs custom tasks when the slideshow changes to the item at the specified index.

## See Also

### Protocols
- [protocol IKCameraDeviceViewDelegate](./ikcameradeviceviewdelegate.md)
  The `IKCameraDeviceViewDelegate` protocol is adopted by the delegate of the [`IKCameraDeviceView`](./ikcameradeviceview.md) class. It allows downloading of camera content, handling selection changes, and handling errors.
- [protocol IKDeviceBrowserViewDelegate](./ikdevicebrowserviewdelegate.md)
  The `IKDeviceBrowserViewDelegate` defines the methods that the delegate of the [`IKDeviceBrowserView`](./ikdevicebrowserview.md) class can implement. All the methods are optional.
- [protocol IKFilterCustomUIProvider](./ikfiltercustomuiprovider.md)
  A protocol used to provide a custom UI.
- [IKImageBrowserDataSource Protocol](./ikimagebrowserdatasource-protocol.md)
  The `IKImageBrowserDataSource` informal protocol declares the methods that an instance of the [`IKImageBrowserView`](./ikimagebrowserview.md)  class uses to access the contents of its data source object.
- [IKImageBrowserDelegate Protocol](./ikimagebrowserdelegate-protocol.md)
  The `IKImageBrowserDelegate` is an informal protocol for the delegate of an [`IKImageBrowserView`](./ikimagebrowserview.md) object. You can implement these methods to perform custom tasks when in response to events in the image browser view.
- [IKImageBrowserItem Protocol](./ikimagebrowseritem-protocol.md)
  The `IKImageBrowserItem` informal protocol declares the methods that an instance of the [`IKImageBrowserView`](./ikimagebrowserview.md) class uses to access the contents of its data source for a given item. Some of the methods in this protocol are needed frequently, so you should implement them efficiently.
- [protocol IKImageEditPanelDataSource](./ikimageeditpaneldatasource.md)
  The `IKImageEditPanelDataSource` protocol describes the methods that an [`IKImageEditPanel`](./ikimageeditpanel.md) object uses to access the contents of its data source object.
- [protocol IKScannerDeviceViewDelegate](./ikscannerdeviceviewdelegate.md)
  The `IKScannerDeviceViewDelegate` protocol defines the delegate protocol that the [`IKScannerDeviceView`](./ikscannerdeviceview.md) delegate must conform to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikslideshowdatasource)*