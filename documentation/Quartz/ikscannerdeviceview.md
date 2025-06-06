# IKScannerDeviceView

**Framework**: Quartz  
**Kind**: class

The `IKScannerDeviceView` class displays a view that allows scanning. It can be customized by specifying the display mode. The delegate receives the scanned data and must implement the [`IKScannerDeviceViewDelegate`](ikscannerdeviceviewdelegate.md) protocol.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
class IKScannerDeviceView
```

## Topics

### Setting the Scanner Device
- [var scannerDevice: ICScannerDevice!](ikscannerdeviceview/scannerdevice.md)
  The device used for scanning
### Setting the Device View’s Display Mode
- [var mode: IKScannerDeviceViewDisplayMode](ikscannerdeviceview/mode.md)
  The display mode used by the device view.
- [var hasDisplayModeAdvanced: Bool](ikscannerdeviceview/hasdisplaymodeadvanced.md)
  The property that determines whether the scanner view uses the advanced display mode.
- [var hasDisplayModeSimple: Bool](ikscannerdeviceview/hasdisplaymodesimple.md)
  The property that determines whether the scanner view uses the simple display mode.
### Configuring Downloading
- [var displaysDownloadsDirectoryControl: Bool](ikscannerdeviceview/displaysdownloadsdirectorycontrol.md)
  Determines whether the downloads directory control is displayed.
- [var downloadsDirectory: URL!](ikscannerdeviceview/downloadsdirectory.md)
  The directory where scans are saved.
- [var transferMode: IKScannerDeviceViewTransferMode](ikscannerdeviceview/transfermode.md)
  Determines how the scanned content is provided to the delegate.
- [var documentName: String!](ikscannerdeviceview/documentname.md)
  Returns the document name.
### Specifying a Post Processing Application
- [var displaysPostProcessApplicationControl: Bool](ikscannerdeviceview/displayspostprocessapplicationcontrol.md)
  Specifies whether the post processing application control is displayed.
- [var postProcessApplication: URL!](ikscannerdeviceview/postprocessapplication.md)
  The URL of the application to use for post processing of the scan.
### Getting and Setting the Delegate
- [var delegate: (any IKScannerDeviceViewDelegate)!](ikscannerdeviceview/delegate.md)
  The scanner device delegate
### Customizing Button Labels
- [var overviewControlLabel: String!](ikscannerdeviceview/overviewcontrollabel.md)
  Allows customization of the “Overview” label.
- [var scanControlLabel: String!](ikscannerdeviceview/scancontrollabel.md)
  Allows customization of the “Scan” label.
### Constants
- [enum IKScannerDeviceViewTransferMode](ikscannerdeviceviewtransfermode.md)
  These constants determine how the scanner data is returned to the delegate. They are used by the [`transferMode`](ikscannerdeviceview/transfermode.md) property.
- [enum IKScannerDeviceViewDisplayMode](ikscannerdeviceviewdisplaymode.md)
  These constants specify the display mode the scanner view will use. They are used by the [`mode`](ikscannerdeviceview/mode.md) property.

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
- [class IKSlideshow](ikslideshow.md)
  The `IKSlideshow` class encapsulates a data source and options for a slideshow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikscannerdeviceview)*