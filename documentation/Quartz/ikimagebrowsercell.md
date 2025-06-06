# IKImageBrowserCell

**Framework**: Quartz  
**Kind**: class

A class used to display a cell.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class IKImageBrowserCell
```

#### Overview

`A` class that is used to display a cell conforming to the [`IKImageBrowserItem Protocol`](ikimagebrowseritem-protocol.md) in an [`IKImageBrowserView`](ikimagebrowserview.md).

## Topics

### Cell Component Frames
- [func frame() -> NSRect](ikimagebrowsercell/frame.md)
  Returns the receiver’s frame rectangle, which defines its position in its [`IKImageBrowserView`](ikimagebrowserview.md).
- [func imageFrame() -> NSRect](ikimagebrowsercell/imageframe.md)
  Returns the receiver’s image frame rectangle, which defines the position of the thumbnail in its [`IKImageBrowserView`](ikimagebrowserview.md).
- [func subtitleFrame() -> NSRect](ikimagebrowsercell/subtitleframe.md)
  Returns the receiver’s subtitle frame rectangle.
- [func titleFrame() -> NSRect](ikimagebrowsercell/titleframe.md)
  Returns the receiver’s title frame rectangle.
- [func imageContainerFrame() -> NSRect](ikimagebrowsercell/imagecontainerframe.md)
  Returns the receiver’s image container frame rectangle, which defines the position of the container of the thumbnail.
### Represented Item
- [func indexOfRepresentedItem() -> Int](ikimagebrowsercell/indexofrepresenteditem.md)
  Returns the index of the receiver’s represented object in the datasource.
- [func representedItem() -> Any!](ikimagebrowsercell/representeditem.md)
  Returns the receiver’s represented object.
### Selection Handling
- [func isSelected() -> Bool](ikimagebrowsercell/isselected.md)
  Returns whether the cell is selected.
- [func selectionFrame() -> NSRect](ikimagebrowsercell/selectionframe.md)
  Returns the receiver’s selection frame rectangle, which defines the position of the selection rectangle in its [`IKImageBrowserView`](ikimagebrowserview.md).
### Cell Content Display
- [func imageAlignment() -> NSImageAlignment](ikimagebrowsercell/imagealignment.md)
  Returns the position of the cell’s image in the frame.
- [func opacity() -> CGFloat](ikimagebrowsercell/opacity.md)
  Returns the opacity of the receiver.
### Getting The Cell State
- [func cellState() -> IKImageBrowserCellState](ikimagebrowsercell/cellstate.md)
  Returns the current cell state of the receiver.
### Core Animation Integration
- [func layer(forType: String!) -> CALayer!](ikimagebrowsercell/layer(fortype:).md)
  Returns a layer for the specified position.
### Getting The Parent Browser View
- [func imageBrowserView() -> IKImageBrowserView!](ikimagebrowsercell/imagebrowserview.md)
  Returns the view the receiver uses to display the cell.
### Constants
- [struct IKImageBrowserCellState](ikimagebrowsercellstate.md)
  The possible states for the browser cell. These values are used by the [`cellState()`](ikimagebrowsercell/cellstate().md) method.
- [Cell Layer Positions](cell-layer-positions.md)
  Optional positioning of additional layers displayed with the cell. Used by the [`layer(forType:)`](ikimagebrowsercell/layer(fortype:).md) method.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class IKCameraDeviceView](ikcameradeviceview.md)
  The `IKCameraDeviceView` class displays the contents of the selected camera.
- [class IKDeviceBrowserView](ikdevicebrowserview.md)
  The `IKDeviceBrowserView` allows you to select a camera or scanner from a list of the available devices.
- [class IKFilterBrowserPanel](ikfilterbrowserpanel.md)
  Presents a user interface for browsing filters.
- [class IKFilterBrowserView](ikfilterbrowserview.md)
  The `IKFilterBrowserView` class is used as a container for the elements of an [`IKFilterBrowserPanel`](ikfilterbrowserpanel.md) object.
- [class IKFilterUIView](ikfilteruiview.md)
  Input parameters for filtering core image filters.
- [class IKImageEditPanel](ikimageeditpanel.md)
  The `IKImageEditPanel` class provides a panel, that is, a utility window that floats on top of document windows, optimized for image editing.
- [class IKImageView](ikimageview.md)
  A view that allows displaying and minor editing of an image.
- [class IKPictureTaker](ikpicturetaker.md)
  The `IKPictureTaker` class represents a panel that allows users to choose images by browsing the file system. The picture taker panel provides an Open Recent menu, supports image cropping, and supports taking snapshots from an iSight or other digital camera.
- [class IKSaveOptions](iksaveoptions.md)
  The `IKSaveOptions` class initializes, adds, and manages user interface options for saving image data.
- [class IKScannerDeviceView](ikscannerdeviceview.md)
  The `IKScannerDeviceView` class displays a view that allows scanning. It can be customized by specifying the display mode. The delegate receives the scanned data and must implement the [`IKScannerDeviceViewDelegate`](ikscannerdeviceviewdelegate.md) protocol.
- [class IKSlideshow](ikslideshow.md)
  The `IKSlideshow` class encapsulates a data source and options for a slideshow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowsercell)*