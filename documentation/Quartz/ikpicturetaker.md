# IKPictureTaker

**Framework**: Quartz  
**Kind**: class

The `IKPictureTaker` class represents a panel that allows users to choose images by browsing the file system. The picture taker panel provides an Open Recent menu, supports image cropping, and supports taking snapshots from an iSight or other digital camera.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class IKPictureTaker
```

## Topics

### Creating And Displaying The Picture Taker
- [class func pictureTaker() -> IKPictureTaker!](ikpicturetaker/picturetaker.md)
  Returns a shared `IKPictureTaker` instance, creating it if necessary.
- [func beginSheet(for: NSWindow!, withDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!)](ikpicturetaker/beginsheet(for:withdelegate:didend:contextinfo:).md)
  Opens a picture taker as a sheet whose parent is the specified window.
- [func begin(withDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!)](ikpicturetaker/begin(withdelegate:didend:contextinfo:).md)
  Opens a picture taker pane.
- [func popUpRecentsMenu(for: NSView!, withDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!)](ikpicturetaker/popuprecentsmenu(for:withdelegate:didend:contextinfo:).md)
  Displays the Open Recent popup menu associated with the  picture taker.
- [func runModal() -> Int](ikpicturetaker/runmodal.md)
  Opens a modal picture taker dialog.
### Getting and Setting Images
- [func setInputImage(NSImage!)](ikpicturetaker/setinputimage(_:).md)
  Set the image input for the picture taker.
- [func inputImage() -> NSImage!](ikpicturetaker/inputimage.md)
  Returns the  input  image associated with the picture taker.
- [func outputImage() -> NSImage!](ikpicturetaker/outputimage.md)
  Returns the edited image.
### Getting and Setting Mirroring
- [func setMirroring(Bool)](ikpicturetaker/setmirroring(_:).md)
  Controls whether the receiver enables video mirroring during snapshots.
- [func mirroring() -> Bool](ikpicturetaker/mirroring.md)
  Returns whether video mirroring is enabled during snapshots.
### Constants
- [Picture Taker Keys](picture-taker-keys.md)
  Keys for customizing the picture taker appearance and behavior. These values are set by sending the picture taker instance `setValue:forKey`.

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
- [class IKImageEditPanel](ikimageeditpanel.md)
  The `IKImageEditPanel` class provides a panel, that is, a utility window that floats on top of document windows, optimized for image editing.
- [class IKImageView](ikimageview.md)
  A view that allows displaying and minor editing of an image.
- [class IKSaveOptions](iksaveoptions.md)
  The `IKSaveOptions` class initializes, adds, and manages user interface options for saving image data.
- [class IKScannerDeviceView](ikscannerdeviceview.md)
  The `IKScannerDeviceView` class displays a view that allows scanning. It can be customized by specifying the display mode. The delegate receives the scanned data and must implement the [`IKScannerDeviceViewDelegate`](ikscannerdeviceviewdelegate.md) protocol.
- [class IKSlideshow](ikslideshow.md)
  The `IKSlideshow` class encapsulates a data source and options for a slideshow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikpicturetaker)*