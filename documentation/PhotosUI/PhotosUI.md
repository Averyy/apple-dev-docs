# PhotosUI

**Framework**: PhotosUI  
**Kind**: module  
**Role**: Framework

Present a person’s photo library using a picker interface, display Live Photos, or extend the Photos app with custom functionality.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 9.0+

#### Overview

PhotosUI offers a photo picker that lets people view their library and choose one or more photos for your app to display or process. The picker renders in a system view and only gives your app access to the photos someone chooses, which facilitates a user experience with enhanced privacy.

The framework also provides a view you can use to display Live Photos.

> **Note**: PhotosUI is a [PhotoKit](../PhotoKit/PhotoKit.md) framework.

## Topics

### Shared photo library
- [Delivering an Enhanced Privacy Experience in Your Photos App](../PhotoKit/delivering-an-enhanced-privacy-experience-in-your-photos-app.md)
  Adopt the latest privacy enhancements to deliver advanced user-privacy controls.
- [class PHLivePhotoView](./phlivephotoview.md)
  A view that displays a Live Photo.
### Photos picker for UIKit, AppKit
- [Selecting Photos and Videos in iOS](../PhotoKit/selecting-photos-and-videos-in-ios.md)
  Improve the user experience of finding and selecting assets by using the Photos picker.
- [class PHPickerViewController](./phpickerviewcontroller.md)
  A view controller that provides the user interface for choosing assets from the photo library.
- [protocol PHPickerViewControllerDelegate](./phpickerviewcontrollerdelegate-5yntc.md)
  A set of methods that the delegate must implement to respond to `PHPickerViewController` user events.
- [struct PHPickerConfiguration](./phpickerconfiguration-swift.struct.md)
  An object that contains information about how to configure a picker view controller.
- [struct PHPickerFilter](./phpickerfilter-swift.struct.md)
  A type that defines the filter to apply to the photo library.
- [struct PHPickerResult](./phpickerresult-swift.struct.md)
  Types that represent a selected asset from a person’s photo library.
### Photos picker for SwiftUI
- [Bringing Photos picker to your SwiftUI app](../PhotoKit/bringing-photos-picker-to-your-swiftui-app.md)
  Select media assets by using a Photos picker view that SwiftUI provides.
- [Implementing an inline Photos picker](../PhotoKit/implementing-an-inline-photos-picker.md)
  Embed a system-provided, half-height Photos picker into your app’s view.
- [struct PhotosPicker](./photospicker.md)
  A view that displays a Photos picker for choosing assets from the photo library.
- [struct PhotosPickerItem](./photospickeritem.md)
  A type that represents an item you use with a Photos picker.
- [struct PhotosPickerSelectionBehavior](./photospickerselectionbehavior.md)
  A type that describes how the Photos picker handles user selection.
- [struct PhotosPickerStyle](./photospickerstyle.md)
### Live Photos
- [Displaying Live Photos](../PhotoKit/displaying-live-photos.md)
  Provide the same interactive playback of Live Photos as in the iOS Photos app.
### Photo editing extensions
- [Creating Photo Editing Extensions](../PhotoKit/creating-photo-editing-extensions.md)
  Provide custom functionality in the Photos app by bundling an app extension.
- [protocol PHContentEditingController](./phcontenteditingcontroller.md)
  A protocol your custom view controller class implements to provide a user interface for your Photos extension.
### macOS Photos project extensions
- [Creating a Slideshow Project Extension for Photos](../PhotoKit/creating-a-slideshow-project-extension-for-photos.md)
  Augment the macOS Photos app with extensions that support project creation.
- [class PHProject](https://developer.apple.com/documentation/photos/phproject)
  A representation of a Photos app project extension.
- [class PHProjectInfo](./phprojectinfo.md)
  Information about the project extension.
- [class PHProjectExtensionContext](./phprojectextensioncontext.md)
  An object that provides Photos project extensions with access to the underlying project, as well as to the user’s photo library for editing.
- [class PHProjectElement](./phprojectelement.md)
  The superclass for all element objects.
- [class PHProjectSection](./phprojectsection.md)
  A collection of content representing curated asset and text elements.
- [class PHProjectRegionOfInterest](./phprojectregionofinterest.md)
  A representation of a region of interest in a photo asset.
- [class PHProjectChangeRequest](https://developer.apple.com/documentation/photos/phprojectchangerequest)
  A request to change asset data in a Photos project extension.
- [protocol PHProjectExtensionController](./phprojectextensioncontroller.md)
  A protocol defining the life cycle and supported types of project extensions.
- [struct PHProjectCategory](./phprojectcategory.md)
  A representation of Photos project extension categories.
### Classes
- [class PHSharedAlbumCreationViewController](./phsharedalbumcreationviewcontroller.md)
- [class PHSharedAlbumCustomizationViewController](./phsharedalbumcustomizationviewcontroller.md)
- [class PHSharedAlbumPostingViewController](./phsharedalbumpostingviewcontroller.md)
### Structures
- [struct PHPickerMetadataOptions](./phpickermetadataoptions.md)
  Constants that specify metadata options for \c PHPickerViewController.
- [struct PHPickerSearchText](./phpickersearchtext-swift.struct.md)
  A search text for `PHPickerViewController`.
- [struct PHSharedAlbumCreationConfiguration](./phsharedalbumcreationconfiguration-swift.struct.md)
  An object used to configure a `PHSharedAlbumCreationViewController`.
- [struct PHSharedAlbumCreationResult](./phsharedalbumcreationresult-swift.struct.md)
  The result of a user creating a shared album.
### Enumerations
- [enum PHSharedAlbumCreationSharingPolicy](./phsharedalbumcreationsharingpolicy.md)
  The sharing policy for creating shared albums.

## See Also

### Frameworks
- [Photos](https://developer.apple.com/documentation/photos)
  Work with image and video assets that the Photos app manages, including those from iCloud Photos and Live Photos.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui)*