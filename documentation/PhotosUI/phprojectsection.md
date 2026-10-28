# PHProjectSection

**Framework**: PhotosUI  
**Kind**: class  
**Role**: Class

A collection of content representing curated asset and text elements.

**Availability**:
- macOS 10.13+

## Declaration

```swift
class PHProjectSection
```

```objc
@interface PHProjectSection : NSObject
```

## Overview

Each project section contains at least one [`PHProjectSectionContent`](./phprojectsectioncontent.md) object, which represents a suggested curation of the content. The number of sections included in [`PHProjectInfo`](./phprojectinfo.md) varies depending on the source used to initialize the project:

- **A Memory.** There will be one cover section with a key asset element and title, as well as a section containing multiple levels of curation, mirroring the Show Summary and Show More options of the Memory in Photos.
- **A single Album.** The number of sections depends on the Album size. A small Album yields a single section, but an Album with a large quantity of photos is broken down into sections based on Moments in the user’s Photo Library.
- **An existing Apple Book, Card, or Calendar.** The sections will match the pagination in that project; for example, a book will break down into one section per page.

## Topics

### Determining Section Contents
- [var title: String](./phprojectsection/title.md)
  The optional section title.
- [var sectionContents: [PHProjectSectionContent]](./phprojectsection/sectioncontents.md)
  An array containing PHProjectionSessionContent objects.
- [class PHProjectSectionContent](./phprojectsectioncontent.md)
  An object containing section elements and layout information for a single level of curation.
### Defining the Section Type
- [var sectionType: PHProjectSection.SectionType](./phprojectsection/sectiontype-swift.property.md)
  The intended usage of the section: cover, content, or auxiliary.
- [PHProjectSection.SectionType](./phprojectsection/sectiontype-swift.enum.md)
  The intended usage of the section: cover, content, or auxiliary.
### Initializers
- [init?(coder: NSCoder)](./phprojectsection/init%28coder%29.md)

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
- [class PHProjectInfo](./phprojectinfo.md)
  Information about the project extension.
- [class PHProjectExtensionContext](./phprojectextensioncontext.md)
  An object that provides Photos project extensions with access to the underlying project, as well as to the user’s photo library for editing.
- [class PHProjectElement](./phprojectelement.md)
  The superclass for all element objects.
- [class PHProjectRegionOfInterest](./phprojectregionofinterest.md)
  A representation of a region of interest in a photo asset.
- [class PHProjectChangeRequest](../Photos/phprojectchangerequest.md)
  A request to change asset data in a Photos project extension.
- [protocol PHProjectExtensionController](./phprojectextensioncontroller.md)
  A protocol defining the life cycle and supported types of project extensions.
- [struct PHProjectCategory](./phprojectcategory.md)
  A representation of Photos project extension categories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojectsection)*