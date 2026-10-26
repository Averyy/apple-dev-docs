# PHProjectCategory

**Framework**: PhotosUI  
**Kind**: struct  
**Role**: Structure

A representation of Photos project extension categories.

**Availability**:
- macOS

## Declaration

```swift
struct PHProjectCategory
```

```c
typedef NSString * PHProjectCategory;
```

#### Overview

This structure encapsulates macOS Photos project extension categories. Use this category to designate the types of projects your extension can create, such as books, calendars, cards, and slideshows.

## Topics

### Creating a Project Category
- [init(rawValue: String)](./phprojectcategory/init%28rawvalue%29.md)
  Intializes a project category from its raw string value.
### Designating Type Properties
- [static let book: PHProjectCategory](./phprojectcategory/book.md)
  The project category for a printed book.
- [static let calendar: PHProjectCategory](./phprojectcategory/calendar.md)
  The project category for a printed calendar.
- [static let card: PHProjectCategory](./phprojectcategory/card.md)
  The project category for a printed card.
- [static let prints: PHProjectCategory](./phprojectcategory/prints.md)
  The project category for physical prints.
- [static let slideshow: PHProjectCategory](./phprojectcategory/slideshow.md)
  The project category for a slideshow.
- [static let wallDecor: PHProjectCategory](./phprojectcategory/walldecor.md)
  The project category for wall décor.
- [static let other: PHProjectCategory](./phprojectcategory/other.md)
  The project category for a custom extension type.
- [static let undefined: PHProjectCategory](./phprojectcategory/undefined.md)
  An undefined project category.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojectcategory)*