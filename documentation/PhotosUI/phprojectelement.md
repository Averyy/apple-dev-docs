# PHProjectElement

**Framework**: PhotosUI  
**Kind**: class  
**Role**: Class

The superclass for all element objects.

**Availability**:
- macOS 10.13+

## Declaration

```swift
class PHProjectElement
```

```objc
@interface PHProjectElement : NSObject
```

#### Overview

You should never use this class directly; opt instead for one of its subclasses. It defines the shared properties of any element in an instance of [`PHProjectSectionContent`](./phprojectsectioncontent.md).

## Topics

### Subclassing Project Elements
- [class PHProjectAssetElement](./phprojectassetelement.md)
  An element that represents a media asset within project section content.
- [class PHProjectTextElement](./phprojecttextelement.md)
  An element that represents text within project section content.
- [class PHProjectJournalEntryElement](./phprojectjournalentryelement.md)
  An element that represents a journal entry within project section content.
- [class PHProjectMapElement](./phprojectmapelement.md)
  An element that represents a map within project section content.
### Describing Project Elements
- [var weight: Double](./phprojectelement/weight.md)
  A value between 0 and 1 representing relative significance of the element in its section.
- [var placement: CGRect](./phprojectelement/placement.md)
  A rectangle defining where an element is placed in grid space coordinates.
### Initializers
- [init?(coder: NSCoder)](./phprojectelement/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [PHProjectAssetElement](./phprojectassetelement.md)
- [PHProjectJournalEntryElement](./phprojectjournalentryelement.md)
- [PHProjectMapElement](./phprojectmapelement.md)
- [PHProjectTextElement](./phprojecttextelement.md)
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
- [class PHProject](https://developer.apple.com/documentation/photos/phproject)
  A representation of a Photos app project extension.
- [class PHProjectInfo](./phprojectinfo.md)
  Information about the project extension.
- [class PHProjectExtensionContext](./phprojectextensioncontext.md)
  An object that provides Photos project extensions with access to the underlying project, as well as to the user’s photo library for editing.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojectelement)*