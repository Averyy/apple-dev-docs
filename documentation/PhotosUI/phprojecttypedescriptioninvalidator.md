# PHProjectTypeDescriptionInvalidator

**Framework**: PhotosUI  
**Kind**: protocol  
**Role**: Protocol

A protocol that you use to tell the project when and how to invalidate type and footer text.

**Availability**:
- macOS 10.14+

## Declaration

```swift
protocol PHProjectTypeDescriptionInvalidator : NSObjectProtocol
```

```objc
@protocol PHProjectTypeDescriptionInvalidator <NSObject>
```

## Overview

An object adheres to this protocol to implement custom behavior when you invalidate project information, such as type description and footer text.

## Topics

### Invalidating a Project Type
- [func invalidateTypeDescription(for: PHProjectType)](./phprojecttypedescriptioninvalidator/invalidatetypedescription%28for%29.md)
  Invalidates the type description for the given project type.
- [func invalidateFooterText(forSubtypesOf: PHProjectType)](./phprojecttypedescriptioninvalidator/invalidatefootertext%28forsubtypesof%29.md)
  Invalidates the footer text for the subtypes of the given project type.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

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
- [PHProjectInfo.CreationSource](./phprojectinfo/creationsource-swift.enum.md)
  Defines the source of a project extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojecttypedescriptioninvalidator)*