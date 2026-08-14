# IKImageEditPanel

**Framework**: Quartz  
**Kind**: class

The `IKImageEditPanel` class provides a panel, that is, a utility window that floats on top of document windows, optimized for image editing.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class IKImageEditPanel
```

## Topics

### Creating an Image Editing Panel
- [class func shared() -> IKImageEditPanel!](ikimageeditpanel/shared.md)
  Creates a shared instance of an image editing panel.
### Getting the User Adjustments and Effects
- [var filterArray: [Any]!](ikimageeditpanel/filterarray.md)
  Returns the current array of user adjustments to effects.
### Getting, Setting, and Reloading Data
- [var dataSource: (any IKImageEditPanelDataSource)!](ikimageeditpanel/datasource.md)
  Specifies the edit panel’s dataSource.
- [func reloadData()](ikimageeditpanel/reloaddata.md)
  Reloads the data from the data associated with an image editing panel.

## Relationships

### Inherits From
- [NSPanel](../appkit/nspanel.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSAccessibilityElementProtocol](../appkit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../appkit/nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](../appkit/nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](../appkit/nsappearancecustomization.md)
- [NSCoding](../foundation/nscoding.md)
- [NSMenuItemValidation](../appkit/nsmenuitemvalidation.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md)
- [NSUserInterfaceValidations](../appkit/nsuserinterfacevalidations.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimageeditpanel)*