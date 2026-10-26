# PHProjectExtensionController

**Framework**: PhotosUI  
**Kind**: protocol  
**Role**: Protocol

A protocol defining the life cycle and supported types of project extensions.

**Availability**:
- macOS 10.13+

## Declaration

```swift
protocol PHProjectExtensionController : NSObjectProtocol
```

```objc
@protocol PHProjectExtensionController <NSObject>
```

#### Overview

The principal view controller for a Photos project extension must conform to this protocol. Methods in this protocol define the basic life cycle of the extension controller. They allow you to define any number of project types that your extension supports; the Photos app displays these project types to the user as choices when creating a new project. To enable this entry point into the extension, the Info.plist must include this key/value pair in its `NSExtensionAttributes` dictionary.

![Screenshot showing the slideshow category in the information property list for a Photos project extension.](https://developer.apple.com/tutorials/images/com.apple.photokit/media-3029168@2x.png)

Once enabled, Photos asks the extension for its list of supported project types. The option that the user selects when creating a project is passed to the extension as an attribute of [`PHProjectInfo`](./phprojectinfo.md).

## Topics

### Tracking the Project Extension Life Cycle
- [func beginProject(with: PHProjectExtensionContext, projectInfo: PHProjectInfo, completion: ((any Error)?) -> Void)](./phprojectextensioncontroller/beginproject%28with,projectinfo,completion%29.md)
  Provides an opportunity to customize the initial state when the user creates a project using the extension.
- [func finishProject(completionHandler: () -> Void)](./phprojectextensioncontroller/finishproject%28completionhandler%29.md)
  Provides an opportunity to perform cleanup when a user switches away from the project or terminates the extension.
- [func resumeProject(with: PHProjectExtensionContext, completion: ((any Error)?) -> Void)](./phprojectextensioncontroller/resumeproject%28with,completion%29.md)
  Provides an opportunity to restore or refresh the user interface when the user returns to a previously created project.
- [func typeDescriptionDataSource(for: PHProjectCategory, invalidator: any PHProjectTypeDescriptionInvalidator) -> any PHProjectTypeDescriptionDataSource](./phprojectextensioncontroller/typedescriptiondatasource%28for,invalidator%29.md)
  Fetches the type description data source to provide the user with more information about the project extension category.
### Defining Supported Project Types
- [var supportedProjectTypes: [PHProjectTypeDescription]](./phprojectextensioncontroller/supportedprojecttypes.md)
  An array of project types the extension supports.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### macOS Photos project extensions
- [Creating a Slideshow Project Extension for Photos](../PhotoKit/creating-a-slideshow-project-extension-for-photos.md)
  Augment the macOS Photos app with extensions that support project creation.
- [class PHProject](../Photos/phproject.md)
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
- [class PHProjectChangeRequest](../Photos/phprojectchangerequest.md)
  A request to change asset data in a Photos project extension.
- [struct PHProjectCategory](./phprojectcategory.md)
  A representation of Photos project extension categories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojectextensioncontroller)*