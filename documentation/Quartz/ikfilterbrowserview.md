# IKFilterBrowserView

**Framework**: Quartz  
**Kind**: class

The `IKFilterBrowserView` class is used as a container for the elements of an [`IKFilterBrowserPanel`](ikfilterbrowserpanel.md) object.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
class IKFilterBrowserView
```

## Topics

### Setting the Preview State
- [func setPreviewState(Bool)](ikfilterbrowserview/setpreviewstate(_:).md)
  Sets the preview state.
### Getting the Filter Name
- [func filterName() -> String!](ikfilterbrowserview/filtername.md)
  Returns the name of the  filter that is currently selected in the filter browser.

## Relationships

### Inherits From
- [NSView](../AppKit/NSView.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/NSAccessibilityElementProtocol.md)
- [NSAccessibilityProtocol](../AppKit/NSAccessibilityProtocol.md)
- [NSAnimatablePropertyContainer](../AppKit/NSAnimatablePropertyContainer.md)
- [NSAppearanceCustomization](../AppKit/NSAppearanceCustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](../AppKit/NSDraggingDestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class IKCameraDeviceView](ikcameradeviceview.md)
  The `IKCameraDeviceView` class displays the contents of the selected camera.
- [class IKDeviceBrowserView](ikdevicebrowserview.md)
  The `IKDeviceBrowserView` allows you to select a camera or scanner from a list of the available devices.
- [class IKFilterBrowserPanel](ikfilterbrowserpanel.md)
  Presents a user interface for browsing filters.
- [class IKFilterUIView](ikfilteruiview.md)
  Input parameters for filtering core image filters.
- [class IKImageBrowserCell](ikimagebrowsercell.md)
  A class used to display a cell.
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

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikfilterbrowserview)*