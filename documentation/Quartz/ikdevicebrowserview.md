# IKDeviceBrowserView

**Framework**: Quartz  
**Kind**: class

The `IKDeviceBrowserView` allows you to select a camera or scanner from a list of the available devices.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
class IKDeviceBrowserView
```

#### Overview

The [`IKDeviceBrowserView`](ikdevicebrowserview.md) delegate must conform to the [`IKDeviceBrowserViewDelegate`](ikdevicebrowserviewdelegate.md) protocol. The delegate provides methods to inform you of selection changes in the browser as well as errors encountered when creating the browser list.

## Topics

### Getting the Selected Device
- [var selectedDevice: ICDevice!](ikdevicebrowserview/selecteddevice.md)
  Returns the selected device.
### Specifying the Device Types to Display
- [var displaysLocalCameras: Bool](ikdevicebrowserview/displayslocalcameras.md)
  Specifies whether local cameras are displayed by the browser.
- [var displaysNetworkCameras: Bool](ikdevicebrowserview/displaysnetworkcameras.md)
  Specifies whether network cameras are displayed by the browser.
- [var displaysLocalScanners: Bool](ikdevicebrowserview/displayslocalscanners.md)
  Specifies whether local scanners are displayed by the browser.
- [var displaysNetworkScanners: Bool](ikdevicebrowserview/displaysnetworkscanners.md)
  Specifies whether network scanners are displayed by the browser.
### Specifying the Display Mode
- [var mode: IKDeviceBrowserViewDisplayMode](ikdevicebrowserview/mode.md)
  Specifies the browser display mode.
### Getting and Setting the Delegate
- [var delegate: (any IKDeviceBrowserViewDelegate)!](ikdevicebrowserview/delegate.md)
  Specifies the delegate object.
### Constants
- [enum IKDeviceBrowserViewDisplayMode](ikdevicebrowserviewdisplaymode.md)
  These constants specify the display mode of the device browser.

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
- [class IKFilterBrowserPanel](ikfilterbrowserpanel.md)
  Presents a user interface for browsing filters.
- [class IKFilterBrowserView](ikfilterbrowserview.md)
  The `IKFilterBrowserView` class is used as a container for the elements of an [`IKFilterBrowserPanel`](ikfilterbrowserpanel.md) object.
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

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikdevicebrowserview)*