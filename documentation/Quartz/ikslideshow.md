# IKSlideshow

**Framework**: Quartz  
**Kind**: class  
**Role**: Class

The `IKSlideshow` class encapsulates a data source and options for a slideshow.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class IKSlideshow
```

```objc
@interface IKSlideshow : NSObject
```

## Topics

### Creating a Shared Instance of a Slideshow
- [class func shared() -> IKSlideshow!](./ikslideshow/shared%28%29.md)
  Returns a shared instance of a slideshow.
### Running and Stopping a Slideshow
- [func run(with: (any IKSlideshowDataSource)!, inMode: String!, options: [AnyHashable : Any]!)](./ikslideshow/run%28with,inmode,options%29.md)
  Runs a slideshow that contains the specified kind of items, provided from a data source.
- [func stop(Any!)](./ikslideshow/stop%28_%29.md)
  Stops a slideshow.
- [var autoPlayDelay: TimeInterval](./ikslideshow/autoplaydelay.md)
  Controls the interval of time before a slideshow starts to play automatically.
### Getting Slideshow Data
- [func indexOfCurrentSlideshowItem() -> Int](./ikslideshow/indexofcurrentslideshowitem%28%29.md)
  Returns the index of the current slideshow item.
### Reloading Data
- [func reloadData()](./ikslideshow/reloaddata%28%29.md)
  Reloads the data for a slideshow.
- [func reloadItem(at: Int)](./ikslideshow/reloaditem%28at%29.md)
  Reloads the data for a slideshow, starting at the specified index.
### Exporting Slideshow Items
- [class func canExport(toApplication: String!) -> Bool](./ikslideshow/canexport%28toapplication%29.md)
  Finds out whether the slideshow can export its contents to an application.
- [class func exportItem(Any!, toApplication: String!)](./ikslideshow/exportitem%28_,toapplication%29.md)
  Exports a slideshow item to the application that has the provided bundle identifier.
### Constants
- [Bundle Identifiers](./bundle-identifiers.md)
  Identifiers for exporting slideshow items to an application.
- [Slideshow Modes](./slideshow-modes.md)
  The kind of items in the slideshow.
- [Slideshow Option Keys](./slideshow-option-keys.md)
  Keys for slideshow options.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Classes
- [class IKCameraDeviceView](./ikcameradeviceview.md)
  The `IKCameraDeviceView` class displays the contents of the selected camera.
- [class IKDeviceBrowserView](./ikdevicebrowserview.md)
  The `IKDeviceBrowserView` allows you to select a camera or scanner from a list of the available devices.
- [class IKFilterBrowserPanel](./ikfilterbrowserpanel.md)
  Presents a user interface for browsing filters.
- [class IKFilterBrowserView](./ikfilterbrowserview.md)
  The `IKFilterBrowserView` class is used as a container for the elements of an [`IKFilterBrowserPanel`](./ikfilterbrowserpanel.md) object.
- [class IKFilterUIView](./ikfilteruiview.md)
  Input parameters for filtering core image filters.
- [class IKImageBrowserCell](./ikimagebrowsercell.md)
  A class used to display a cell.
- [class IKImageEditPanel](./ikimageeditpanel.md)
  The `IKImageEditPanel` class provides a panel, that is, a utility window that floats on top of document windows, optimized for image editing.
- [class IKImageView](./ikimageview.md)
  A view that allows displaying and minor editing of an image.
- [class IKPictureTaker](./ikpicturetaker.md)
  The `IKPictureTaker` class represents a panel that allows users to choose images by browsing the file system. The picture taker panel provides an Open Recent menu, supports image cropping, and supports taking snapshots from an iSight or other digital camera.
- [class IKSaveOptions](./iksaveoptions.md)
  The `IKSaveOptions` class initializes, adds, and manages user interface options for saving image data.
- [class IKScannerDeviceView](./ikscannerdeviceview.md)
  The `IKScannerDeviceView` class displays a view that allows scanning. It can be customized by specifying the display mode. The delegate receives the scanned data and must implement the [`IKScannerDeviceViewDelegate`](./ikscannerdeviceviewdelegate.md) protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikslideshow)*