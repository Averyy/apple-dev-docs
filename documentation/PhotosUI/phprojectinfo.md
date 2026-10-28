# PHProjectInfo

**Framework**: PhotosUI  
**Kind**: class  
**Role**: Class

Information about the project extension.

**Availability**:
- macOS 10.13+

## Declaration

```swift
class PHProjectInfo
```

```objc
@interface PHProjectInfo : NSObject
```

## Overview

macOS Photos automatically generates a [`PHProjectInfo`](./phprojectinfo.md) object when creating a new project. Photos passes along the project information with a [`PHProjectExtensionContext`](./phprojectextensioncontext.md) object. This object contains metadata about the project’s creation source, sections, product type, branding, and page numbers. Your extension leverages project information to influence project layout, autoflow, and theme selection. The properties of this class are immutable, and your extension can’t instantiate the object directly.

## Topics

### Determining Project Type
- [var projectType: PHProjectType](./phprojectinfo/projecttype.md)
  The project type that the user selected from the project extension options.
- [struct PHProjectType](./phprojecttype.md)
  The type descriptor of a project extension.
- [var creationSource: PHProjectInfo.CreationSource](./phprojectinfo/creationsource-swift.property.md)
  The source from which the project was created.
- [var sections: [PHProjectSection]](./phprojectinfo/sections.md)
  An array of project sections, each containing one or more section content objects.
- [class PHProjectTypeDescription](./phprojecttypedescription.md)
  An extensible enumerator for [`PHProjectType`](./phprojecttype.md) that’s presented to users in the project picker.
- [protocol PHProjectTypeDescriptionDataSource](./phprojecttypedescriptiondatasource.md)
  A protocol that you use to provide the project with type description data.
- [protocol PHProjectTypeDescriptionInvalidator](./phprojecttypedescriptioninvalidator.md)
  A protocol that you use to tell the project when and how to invalidate type and footer text.
- [PHProjectInfo.CreationSource](./phprojectinfo/creationsource-swift.enum.md)
  Defines the source of a project extension.
### Creating a Project from an Apple Print Product
- [var brandingEnabled: Bool](./phprojectinfo/brandingenabled.md)
  A Boolean value indicating whether branding was enabled in the source project.
- [var pageNumbersEnabled: Bool](./phprojectinfo/pagenumbersenabled.md)
  A Boolean value indicating whether page numbering was enabled in the source project.
- [var productIdentifier: String?](./phprojectinfo/productidentifier.md)
  The product identifier of the originating Apple Print Product.
- [var themeIdentifier: String?](./phprojectinfo/themeidentifier.md)
  The product theme identifier of the originating Apple Print Product.
### Initializers
- [init?(coder: NSCoder)](./phprojectinfo/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### macOS Photos project extensions
- [Creating a Slideshow Project Extension for Photos](../PhotoKit/creating-a-slideshow-project-extension-for-photos.md)
  Augment the macOS Photos app with extensions that support project creation.
- [class PHProject](../Photos/phproject.md)
  A representation of a Photos app project extension.
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
- [protocol PHProjectExtensionController](./phprojectextensioncontroller.md)
  A protocol defining the life cycle and supported types of project extensions.
- [struct PHProjectCategory](./phprojectcategory.md)
  A representation of Photos project extension categories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojectinfo)*