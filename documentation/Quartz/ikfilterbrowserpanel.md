# IKFilterBrowserPanel

**Framework**: Quartz  
**Kind**: class

Presents a user interface for browsing filters.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
class IKFilterBrowserPanel
```

#### Overview

The `IKFilterBrowserPanel` class provides a user interface that allows users to browse Core Image filters ([`CIFilter`](https://developer.apple.com/documentation/coreimage/cifilter)), to preview a filter, and to get additional information about the filter, such as its description.

An `IKFilterBrowserPanel` object can be displayed as:

- a separate panel, that is, a utility window that floats on top of document windows
- a modal dialog
- a sheet, that is, a dialog that is attached to its parent window and must be dismissed by the user
- a view that an application can insert into a custom user  interface

An `IKFilterBrowserPanel` object can be configured through a style mask to use either the default or brushed metal look for windows. The size and number of visible controls are specified through an options dictionary. An `IKFilterBrowserPanel` object communicates selection changes through notifications.

The `IKFilterBrowserPanel` class allows the user to create filter collections that are stored with the `filterCollections` key in the `com.apple.CoreImageKit.plist` property list located in `~/Library/Preferences/`.

## Topics

### Getting a Filter Name
- [func filterName() -> String!](ikfilterbrowserpanel/filtername.md)
  Returns the name of the  filter that is currently selected in the filter browser.
### Displaying and Running the Panel
- [func filterBrowserView(options: [AnyHashable : Any]!) -> IKFilterBrowserView!](ikfilterbrowserpanel/filterbrowserview(options:).md)
  Returns a view that contains a filter browser.
- [func begin(options: [AnyHashable : Any]!, modelessDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!)](ikfilterbrowserpanel/begin(options:modelessdelegate:didend:contextinfo:).md)
  Displays the filter browser in a new utility window, unless the filter browser is already open.
- [func beginSheet(options: [AnyHashable : Any]!, modalFor: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!)](ikfilterbrowserpanel/beginsheet(options:modalfor:modaldelegate:didend:contextinfo:).md)
  Displays the filter browser in a sheet—that is, a dialog that is attached to its parent window and must be dismissed by the user.
- [func runModal(options: [AnyHashable : Any]!) -> Int32](ikfilterbrowserpanel/runmodal(options:).md)
  Displays the filter browser in a modal dialog that must be dismissed by the user but that is not  attached to a window.
- [func finish(Any!)](ikfilterbrowserpanel/finish(_:).md)
  Closes a filter browser view.
### Creating a Filter Browser Panel
- [class func filterBrowserPanel(withStyleMask: UInt32) -> Any!](ikfilterbrowserpanel/filterbrowserpanel(withstylemask:).md)
  Creates a shared instance of the `IKFilterBrowserPanel` class.
### Constants
- [Filter Browser Option Keys](filter-browser-option-keys.md)
  Keys for filter browser options.

## Relationships

### Inherits From
- [NSPanel](../AppKit/NSPanel.md)
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
- [NSMenuItemValidation](../AppKit/NSMenuItemValidation.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)
- [NSUserInterfaceValidations](../AppKit/NSUserInterfaceValidations.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class IKCameraDeviceView](ikcameradeviceview.md)
  The `IKCameraDeviceView` class displays the contents of the selected camera.
- [class IKDeviceBrowserView](ikdevicebrowserview.md)
  The `IKDeviceBrowserView` allows you to select a camera or scanner from a list of the available devices.
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

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikfilterbrowserpanel)*