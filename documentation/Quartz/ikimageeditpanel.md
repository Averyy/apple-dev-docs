# IKImageEditPanel

**Framework**: Quartz  
**Kind**: class  
**Role**: Class

The `IKImageEditPanel` class provides a panel, that is, a utility window that floats on top of document windows, optimized for image editing.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class IKImageEditPanel
```

```objc
@interface IKImageEditPanel : NSPanel
```

## Topics

### Creating an Image Editing Panel
- [class func shared() -> IKImageEditPanel!](./ikimageeditpanel/shared%28%29.md)
  Creates a shared instance of an image editing panel.
### Getting the User Adjustments and Effects
- [var filterArray: [Any]!](./ikimageeditpanel/filterarray.md)
  Returns the current array of user adjustments to effects.
### Getting, Setting, and Reloading Data
- [var dataSource: (any IKImageEditPanelDataSource)!](./ikimageeditpanel/datasource.md)
  Specifies the edit panel’s dataSource.
- [func reloadData()](./ikimageeditpanel/reloaddata%28%29.md)
  Reloads the data from the data associated with an image editing panel.

## Relationships

### Inherits From
- [NSPanel](../AppKit/nspanel.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../AppKit/nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](../AppKit/nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](../AppKit/nsappearancecustomization.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSMenuItemValidation](../AppKit/nsmenuitemvalidation.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/nsuserinterfaceitemidentification.md)
- [NSUserInterfaceValidations](../AppKit/nsuserinterfacevalidations.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

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
- [class IKImageView](./ikimageview.md)
  A view that allows displaying and minor editing of an image.
- [class IKPictureTaker](./ikpicturetaker.md)
  The `IKPictureTaker` class represents a panel that allows users to choose images by browsing the file system. The picture taker panel provides an Open Recent menu, supports image cropping, and supports taking snapshots from an iSight or other digital camera.
- [class IKSaveOptions](./iksaveoptions.md)
  The `IKSaveOptions` class initializes, adds, and manages user interface options for saving image data.
- [class IKScannerDeviceView](./ikscannerdeviceview.md)
  The `IKScannerDeviceView` class displays a view that allows scanning. It can be customized by specifying the display mode. The delegate receives the scanned data and must implement the [`IKScannerDeviceViewDelegate`](./ikscannerdeviceviewdelegate.md) protocol.
- [class IKSlideshow](./ikslideshow.md)
  The `IKSlideshow` class encapsulates a data source and options for a slideshow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimageeditpanel)*