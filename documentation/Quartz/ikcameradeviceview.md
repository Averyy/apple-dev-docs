# IKCameraDeviceView

**Framework**: Quartz  
**Kind**: class

The `IKCameraDeviceView` class displays the contents of the selected camera.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
class IKCameraDeviceView
```

## Topics

### Getting and Setting the Camera Device
- [var cameraDevice: ICCameraDevice!](ikcameradeviceview/cameradevice.md)
  The current camera device.
### View Display Mode
- [var iconSize: Int](ikcameradeviceview/iconsize.md)
  Specifies the icon size.
- [var mode: IKCameraDeviceViewDisplayMode](ikcameradeviceview/mode.md)
  Specifies the display mode of the camera device view.
- [var hasDisplayModeIcon: Bool](ikcameradeviceview/hasdisplaymodeicon.md)
  Returns whether the device view is being displayed in icon mode.
- [var hasDisplayModeTable: Bool](ikcameradeviceview/hasdisplaymodetable.md)
  Returns whether the device view is being displayed in table mode.
### Selecting the File Transfer Mode
- [var transferMode: IKCameraDeviceViewTransferMode](ikcameradeviceview/transfermode.md)
  Determines how the contents are saved by the delegate.
### Configuring Download Interface and Downloading Files
- [var canDownloadSelectedItems: Bool](ikcameradeviceview/candownloadselecteditems.md)
  Returns whether the selected items can be downloaded
- [var downloadsDirectory: URL!](ikcameradeviceview/downloadsdirectory.md)
  Specifies the directory where files are downloaded
- [func downloadSelectedItems(Any!)](ikcameradeviceview/downloadselecteditems(_:).md)
  Deletes the selected items from the camera.
- [func downloadAllItems(Any!)](ikcameradeviceview/downloadallitems(_:).md)
  Downloads all the items.
- [var downloadSelectedControlLabel: String!](ikcameradeviceview/downloadselectedcontrollabel.md)
  Allows the “Download Selected” control to be renamed.
- [var downloadAllControlLabel: String!](ikcameradeviceview/downloadallcontrollabel.md)
  Allows the “Download All” control to be renamed.
- [var displaysDownloadsDirectoryControl: Bool](ikcameradeviceview/displaysdownloadsdirectorycontrol.md)
  Specifies whether the downloads directory control should be displayed.
### Getting and Setting the Post Processing Application
- [var displaysPostProcessApplicationControl: Bool](ikcameradeviceview/displayspostprocessapplicationcontrol.md)
  Displays whether the post process application control should be displayed.
- [var postProcessApplication: URL!](ikcameradeviceview/postprocessapplication.md)
  The URL of the application used to post process the image.
### Deleting Selected Items
- [var canDeleteSelectedItems: Bool](ikcameradeviceview/candeleteselecteditems.md)
  Returns whether the selected items can be deleted.
- [func deleteSelectedItems(Any!)](ikcameradeviceview/deleteselecteditems(_:).md)
  Deletes the currently selected items.
### Selection Management
- [func select(IndexSet!, byExtendingSelection: Bool)](ikcameradeviceview/select(_:byextendingselection:).md)
  Invoked to select the specified files, extending the selection if specified.
- [func selectedIndexes() -> IndexSet!](ikcameradeviceview/selectedindexes.md)
  The selected indexes of the camera files.
### Getting and Setting the Delegate
- [var delegate: (any IKCameraDeviceViewDelegate)!](ikcameradeviceview/delegate.md)
  The camera device view delegate.
### Selected Item Rotation
- [var canRotateSelectedItemsLeft: Bool](ikcameradeviceview/canrotateselecteditemsleft.md)
  Returns whether the selected items can be rotated left.
- [var canRotateSelectedItemsRight: Bool](ikcameradeviceview/canrotateselecteditemsright.md)
  Returns whether the selected items can be rotated right.
- [func rotateLeft(Any!)](ikcameradeviceview/rotateleft(_:).md)
  Rotates the selected image to the left.
- [func rotateRight(Any!)](ikcameradeviceview/rotateright(_:).md)
  Rotates the selected image to the right.
### Constants
- [enum IKCameraDeviceViewDisplayMode](ikcameradeviceviewdisplaymode.md)
  These constants specify the display mode used by the camera view. These constants are used by [`mode`](ikcameradeviceview/mode.md).
- [enum IKCameraDeviceViewTransferMode](ikcameradeviceviewtransfermode.md)
  These constants specify the transfer mode used by the camera view. These constants are used by [`mode`](ikcameradeviceview/mode.md).
### Instance Methods
- [func setCustomActionControl(NSSegmentedControl!)](ikcameradeviceview/setcustomactioncontrol(_:).md)
- [func setCustomDelete(NSSegmentedControl!)](ikcameradeviceview/setcustomdelete(_:).md)
- [func setCustomIconSizeSlider(NSSlider!)](ikcameradeviceview/setcustomiconsizeslider(_:).md)
- [func setCustomModeControl(NSSegmentedControl!)](ikcameradeviceview/setcustommodecontrol(_:).md)
- [func setCustomRotateControl(NSSegmentedControl!)](ikcameradeviceview/setcustomrotatecontrol(_:).md)
- [func setShowStatusInfoAsWindowSubtitle(Bool)](ikcameradeviceview/setshowstatusinfoaswindowsubtitle(_:).md)

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
- [class IKScannerDeviceView](ikscannerdeviceview.md)
  The `IKScannerDeviceView` class displays a view that allows scanning. It can be customized by specifying the display mode. The delegate receives the scanned data and must implement the [`IKScannerDeviceViewDelegate`](ikscannerdeviceviewdelegate.md) protocol.
- [class IKSlideshow](ikslideshow.md)
  The `IKSlideshow` class encapsulates a data source and options for a slideshow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikcameradeviceview)*