# IKPictureTaker

**Framework**: Quartz  
**Kind**: class  
**Role**: Class

The `IKPictureTaker` class represents a panel that allows users to choose images by browsing the file system. The picture taker panel provides an Open Recent menu, supports image cropping, and supports taking snapshots from an iSight or other digital camera.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class IKPictureTaker
```

```objc
@interface IKPictureTaker : NSPanel
```

## Topics

### Creating And Displaying The Picture Taker
- [class func pictureTaker() -> IKPictureTaker!](./ikpicturetaker/picturetaker%28%29.md)
  Returns a shared `IKPictureTaker` instance, creating it if necessary.
- [func beginSheet(for: NSWindow!, withDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!)](./ikpicturetaker/beginsheet%28for,withdelegate,didend,contextinfo%29.md)
  Opens a picture taker as a sheet whose parent is the specified window.
- [func begin(withDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!)](./ikpicturetaker/begin%28withdelegate,didend,contextinfo%29.md)
  Opens a picture taker pane.
- [func popUpRecentsMenu(for: NSView!, withDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!)](./ikpicturetaker/popuprecentsmenu%28for,withdelegate,didend,contextinfo%29.md)
  Displays the Open Recent popup menu associated with the  picture taker.
- [func runModal() -> Int](./ikpicturetaker/runmodal%28%29.md)
  Opens a modal picture taker dialog.
### Getting and Setting Images
- [func setInputImage(NSImage!)](./ikpicturetaker/setinputimage%28_%29.md)
  Set the image input for the picture taker.
- [func inputImage() -> NSImage!](./ikpicturetaker/inputimage%28%29.md)
  Returns the  input  image associated with the picture taker.
- [func outputImage() -> NSImage!](./ikpicturetaker/outputimage%28%29.md)
  Returns the edited image.
### Getting and Setting Mirroring
- [func setMirroring(Bool)](./ikpicturetaker/setmirroring%28_%29.md)
  Controls whether the receiver enables video mirroring during snapshots.
- [func mirroring() -> Bool](./ikpicturetaker/mirroring%28%29.md)
  Returns whether video mirroring is enabled during snapshots.
### Constants
- [Picture Taker Keys](./picture-taker-keys.md)
  Keys for customizing the picture taker appearance and behavior. These values are set by sending the picture taker instance `setValue:forKey`.

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
- [class IKImageEditPanel](./ikimageeditpanel.md)
  The `IKImageEditPanel` class provides a panel, that is, a utility window that floats on top of document windows, optimized for image editing.
- [class IKImageView](./ikimageview.md)
  A view that allows displaying and minor editing of an image.
- [class IKSaveOptions](./iksaveoptions.md)
  The `IKSaveOptions` class initializes, adds, and manages user interface options for saving image data.
- [class IKScannerDeviceView](./ikscannerdeviceview.md)
  The `IKScannerDeviceView` class displays a view that allows scanning. It can be customized by specifying the display mode. The delegate receives the scanned data and must implement the [`IKScannerDeviceViewDelegate`](./ikscannerdeviceviewdelegate.md) protocol.
- [class IKSlideshow](./ikslideshow.md)
  The `IKSlideshow` class encapsulates a data source and options for a slideshow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikpicturetaker)*