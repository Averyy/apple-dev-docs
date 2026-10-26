# PHProjectExtensionContext

**Framework**: PhotosUI  
**Kind**: class  
**Role**: Class

An object that provides Photos project extensions with access to the underlying project, as well as to the user’s photo library for editing.

**Availability**:
- macOS 10.13+

## Declaration

```swift
class PHProjectExtensionContext
```

```objc
@interface PHProjectExtensionContext : NSExtensionContext
```

#### Overview

When a Photos project extension is initialized, it is handed an extension context object. This object provides the extension with access to the underlying project, as well as the photo library from which assets are fetched and edited.

## Topics

### Accessing the Project and the Photo Library
- [var project: PHProject](./phprojectextensioncontext/project.md)
  A read-only version of the project being edited.
- [var photoLibrary: PHPhotoLibrary](./phprojectextensioncontext/photolibrary.md)
  A read-only version of the photo library being modified.
### Updating Assets
- [func showEditor(for: PHAsset)](./phprojectextensioncontext/showeditor%28for%29.md)
  Invokes the built-in photo editor for the given asset.
- [func updatedProjectInfo(from: PHProjectInfo?, completion: (PHProjectInfo?) -> Void) -> Progress](./phprojectextensioncontext/updatedprojectinfo%28from,completion%29.md)
  Creates an updated [`PHProjectInfo`](./phprojectinfo.md) instance from existing project information and current assets.

## Relationships

### Inherits From
- [NSExtensionContext](../Foundation/nsextensioncontext.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### macOS Photos project extensions
- [Creating a Slideshow Project Extension for Photos](../PhotoKit/creating-a-slideshow-project-extension-for-photos.md)
  Augment the macOS Photos app with extensions that support project creation.
- [class PHProject](../Photos/phproject.md)
  A representation of a Photos app project extension.
- [class PHProjectInfo](./phprojectinfo.md)
  Information about the project extension.
- [class PHProjectElement](./phprojectelement.md)
  The superclass for all element objects.
- [class PHProjectSection](./phprojectsection.md)
  A collection of content representing curated asset and text elements.
- [class PHProjectRegionOfInterest](./phprojectregionofinterest.md)
  A representation of a region of interest in a photo asset.
- [class PHProjectChangeRequest](../Photos/phprojectchangerequest.md)
  A request to change asset data in a Photos project extension.
- [protocol PHProjectExtensionController](./phprojectextensioncontroller.md)
  A protocol defining the life cycle and supported types of project extensions.
- [struct PHProjectCategory](./phprojectcategory.md)
  A representation of Photos project extension categories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojectextensioncontext)*