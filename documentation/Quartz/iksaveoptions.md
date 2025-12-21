# IKSaveOptions

**Framework**: Quartz  
**Kind**: class

The `IKSaveOptions` class initializes, adds, and manages user interface options for saving image data.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class IKSaveOptions
```

## Topics

### Creating A Save Options Accessory View
- [init!(imageProperties: [AnyHashable : Any]!, imageUTType: String!)](iksaveoptions/init(imageproperties:imageuttype:).md)
  Initializes a save options accessory pane for the provided image properties and uniform type identifier.
- [func addAccessoryView(to: NSSavePanel!)](iksaveoptions/addaccessoryview(to:).md)
  Adds `IKSaveOptions` accessory view to a `NSSavePanel`.
### Retrieving User Responses
- [var imageProperties: [AnyHashable : Any]!](iksaveoptions/imageproperties.md)
  Returns a dictionary of updated image properties that reflects the user’s selection.
- [var imageUTType: String!](iksaveoptions/imageuttype.md)
  Returns the uniform type identifier that reflects the user’s selection.
- [var userSelection: [AnyHashable : Any]!](iksaveoptions/userselection.md)
  Returns a dictionary that contains the save options selected by the user.
### Getting and Setting the delegate
- [var delegate: AnyObject!](iksaveoptions/delegate.md)
  Specifies the delegate object.
### File Type Filtering
- [func saveOptions(IKSaveOptions!, shouldShowUTType: String!) -> Bool](../ObjectiveC/NSObject-swift.class/saveOptions(_:shouldShowUTType:).md)
  Called to determine if the specified uniform type identifier should be shown in the save panel.
### Instance Properties
- [var rememberLastSetting: Bool](iksaveoptions/rememberlastsetting.md)
### Instance Methods
- [func add(to: NSView!)](iksaveoptions/add(to:).md)

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
- [class IKImageBrowserCell](ikimagebrowsercell.md)
  A class used to display a cell.
- [class IKImageEditPanel](ikimageeditpanel.md)
  The `IKImageEditPanel` class provides a panel, that is, a utility window that floats on top of document windows, optimized for image editing.
- [class IKImageView](ikimageview.md)
  A view that allows displaying and minor editing of an image.
- [class IKPictureTaker](ikpicturetaker.md)
  The `IKPictureTaker` class represents a panel that allows users to choose images by browsing the file system. The picture taker panel provides an Open Recent menu, supports image cropping, and supports taking snapshots from an iSight or other digital camera.
- [class IKScannerDeviceView](ikscannerdeviceview.md)
  The `IKScannerDeviceView` class displays a view that allows scanning. It can be customized by specifying the display mode. The delegate receives the scanned data and must implement the [`IKScannerDeviceViewDelegate`](ikscannerdeviceviewdelegate.md) protocol.
- [class IKSlideshow](ikslideshow.md)
  The `IKSlideshow` class encapsulates a data source and options for a slideshow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/iksaveoptions)*