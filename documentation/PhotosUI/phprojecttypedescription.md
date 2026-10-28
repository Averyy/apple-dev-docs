# PHProjectTypeDescription

**Framework**: PhotosUI  
**Kind**: class  
**Role**: Class

An extensible enumerator for [`PHProjectType`](./phprojecttype.md) that’s presented to users in the project picker.

**Availability**:
- macOS 10.13+

## Declaration

```swift
class PHProjectTypeDescription
```

```objc
@interface PHProjectTypeDescription : NSObject
```

## Overview

This object represents one project type choice presented in the project picker when a user is creating a project through project extensions. The [`PHProjectTypeDescriptionDataSource`](./phprojecttypedescriptiondatasource.md) object returns this descriptor from [`typeDescriptionDataSource(for:invalidator:)`](./phprojectextensioncontroller/typedescriptiondatasource%28for,invalidator%29.md).

## Topics

### Creating a Project Type Description
- [convenience init(projectType: PHProjectType, title: String, description: String?, image: NSImage?)](./phprojecttypedescription/init%28projecttype,title,description,image%29.md)
  A convenience initializer without subtype descriptions.
- [init(projectType: PHProjectType, title: String, description: String?, image: NSImage?, subtypeDescriptions: [PHProjectTypeDescription])](./phprojecttypedescription/init%28projecttype,title,description,image,subtypedescriptions%29.md)
  A designated initializer for project type descriptions with the full subtype hierarchy specified up front and a standard string for description text.
- [init(projectType: PHProjectType, title: String, attributedDescription: NSAttributedString?, image: NSImage?, subtypeDescriptions: [PHProjectTypeDescription])](./phprojecttypedescription/init%28projecttype,title,attributeddescription,image,subtypedescriptions%29.md)
  A designated initializer for project type descriptions with the full subtype hierarchy specified up front and an attributed string for description text.
- [init(projectType: PHProjectType, title: String, description: String?, image: NSImage?, canProvideSubtypes: Bool)](./phprojecttypedescription/init%28projecttype,title,description,image,canprovidesubtypes%29.md)
  A designated initializer for project type descriptions with lazily fetched subtypes and a standard description string.
- [init(projectType: PHProjectType, title: String, attributedDescription: NSAttributedString?, image: NSImage?, canProvideSubtypes: Bool)](./phprojecttypedescription/init%28projecttype,title,attributeddescription,image,canprovidesubtypes%29.md)
  A designated initializer for project type descriptions with lazily fetched subtypes and an attributed description string.
### Describing a Project Type
- [var projectType: PHProjectType](./phprojecttypedescription/projecttype.md)
  An identifier for the project type.
- [var localizedTitle: String](./phprojecttypedescription/localizedtitle.md)
  The localized title of the project type as shown to the user.
- [var localizedDescription: String?](./phprojecttypedescription/localizeddescription.md)
  The localized description of the project type as shown to the user.
- [var localizedAttributedDescription: NSAttributedString?](./phprojecttypedescription/localizedattributeddescription.md)
  The localized attributed description of the project type as shown to the user.
- [var image: NSImage?](./phprojecttypedescription/image.md)
  An optional image associated with the project type in the picker.
- [var subtypeDescriptions: [PHProjectTypeDescription]](./phprojecttypedescription/subtypedescriptions.md)
  An array of type descriptions used for subtype descriptions.
- [var canProvideSubtypes: Bool](./phprojecttypedescription/canprovidesubtypes.md)
  A Boolean variable indicating whether subtypes can be fetched from the data source.
### Initializers
- [init?(coder: NSCoder)](./phprojecttypedescription/init%28coder%29.md)

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

### Determining Project Type
- [var projectType: PHProjectType](./phprojectinfo/projecttype.md)
  The project type that the user selected from the project extension options.
- [struct PHProjectType](./phprojecttype.md)
  The type descriptor of a project extension.
- [var creationSource: PHProjectInfo.CreationSource](./phprojectinfo/creationsource-swift.property.md)
  The source from which the project was created.
- [var sections: [PHProjectSection]](./phprojectinfo/sections.md)
  An array of project sections, each containing one or more section content objects.
- [protocol PHProjectTypeDescriptionDataSource](./phprojecttypedescriptiondatasource.md)
  A protocol that you use to provide the project with type description data.
- [protocol PHProjectTypeDescriptionInvalidator](./phprojecttypedescriptioninvalidator.md)
  A protocol that you use to tell the project when and how to invalidate type and footer text.
- [PHProjectInfo.CreationSource](./phprojectinfo/creationsource-swift.enum.md)
  Defines the source of a project extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojecttypedescription)*