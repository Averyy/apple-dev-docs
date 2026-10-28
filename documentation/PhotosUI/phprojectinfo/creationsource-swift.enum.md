# PHProjectInfo.CreationSource

**Framework**: PhotosUI  
**Kind**: enum  
**Role**: Enumeration

Defines the source of a project extension.

**Availability**:
- macOS 10.13+

## Declaration

```swift
enum CreationSource
```

```c
enum PHProjectCreationSource : NSInteger;
```

## Overview

Each source represents a file type from which users can create a project extension.

## Topics

### Project Sources
- [PHProjectInfo.CreationSource.undefined](./creationsource-swift.enum/undefined.md)
  An undefined project extension.
- [PHProjectInfo.CreationSource.userSelection](./creationsource-swift.enum/userselection.md)
  A project extension created from a user selection of photos.
- [PHProjectInfo.CreationSource.album](./creationsource-swift.enum/album.md)
  A project extension created from a photo album.
- [PHProjectInfo.CreationSource.memory](./creationsource-swift.enum/memory.md)
  A project extension created from a memory.
- [PHProjectInfo.CreationSource.moment](./creationsource-swift.enum/moment.md)
  A project extension created from a moment.
- [PHProjectInfo.CreationSource.project](./creationsource-swift.enum/project.md)
  A project extension created from an existing Photos project.
- [PHProjectInfo.CreationSource.projectBook](./creationsource-swift.enum/projectbook.md)
  A project extension created from a Photos project book.
- [PHProjectInfo.CreationSource.projectCalendar](./creationsource-swift.enum/projectcalendar.md)
  A project extension created from a calendar.
- [PHProjectInfo.CreationSource.projectCard](./creationsource-swift.enum/projectcard.md)
  A project extension created from a card.
- [PHProjectInfo.CreationSource.projectPrintOrder](./creationsource-swift.enum/projectprintorder.md)
  A project extension created from a print order.
- [PHProjectInfo.CreationSource.projectSlideshow](./creationsource-swift.enum/projectslideshow.md)
  A project slideshow extension.
- [PHProjectInfo.CreationSource.projectExtension](./creationsource-swift.enum/projectextension.md)
  A project extension created from another project extension.
### Initializers
- [init?(rawValue: Int)](./creationsource-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Determining Project Type
- [var projectType: PHProjectType](./projecttype.md)
  The project type that the user selected from the project extension options.
- [struct PHProjectType](../phprojecttype.md)
  The type descriptor of a project extension.
- [var creationSource: PHProjectInfo.CreationSource](./creationsource-swift.property.md)
  The source from which the project was created.
- [var sections: [PHProjectSection]](./sections.md)
  An array of project sections, each containing one or more section content objects.
- [class PHProjectTypeDescription](../phprojecttypedescription.md)
  An extensible enumerator for [`PHProjectType`](../phprojecttype.md) that’s presented to users in the project picker.
- [protocol PHProjectTypeDescriptionDataSource](../phprojecttypedescriptiondatasource.md)
  A protocol that you use to provide the project with type description data.
- [protocol PHProjectTypeDescriptionInvalidator](../phprojecttypedescriptioninvalidator.md)
  A protocol that you use to tell the project when and how to invalidate type and footer text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojectinfo/creationsource-swift.enum)*