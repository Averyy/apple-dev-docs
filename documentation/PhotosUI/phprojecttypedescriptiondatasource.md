# PHProjectTypeDescriptionDataSource

**Framework**: PhotosUI  
**Kind**: protocol  
**Role**: Protocol

A protocol that you use to provide the project with type description data.

**Availability**:
- macOS 10.14+

## Declaration

```swift
protocol PHProjectTypeDescriptionDataSource : NSObjectProtocol
```

```objc
@protocol PHProjectTypeDescriptionDataSource <NSObject>
```

#### Overview

An object adheres to this protocol to provide a type description for your app’s Photos project extension. You must implement this protocol to provide subtypes, a description, and footer text. You can optionally respond to the system discarding the data source by implementing [`extensionWillDiscardDataSource()`](./phprojecttypedescriptiondatasource/extensionwilldiscarddatasource%28%29.md).

## Topics

### Providing Required Fields
- [func subtypes(for: PHProjectType) -> [PHProjectTypeDescription]](./phprojecttypedescriptiondatasource/subtypes%28for%29.md)
  Provides the root-level project type descriptions and descriptions of any promised subtypes with [`canProvideSubtypes`](./phprojecttypedescription/canprovidesubtypes.md) set to `true`.
- [func typeDescription(for: PHProjectType) -> PHProjectTypeDescription?](./phprojecttypedescriptiondatasource/typedescription%28for%29.md)
  Provides the updated project type description for previously invalidated project types.
- [func footerText(forSubtypesOf: PHProjectType) -> NSAttributedString?](./phprojecttypedescriptiondatasource/footertext%28forsubtypesof%29.md)
  Provides the footer text for the subtypes of the given project type.
### Responding to Removal
- [func extensionWillDiscardDataSource()](./phprojecttypedescriptiondatasource/extensionwilldiscarddatasource%28%29.md)
  Provides an opportunity to use the data source before it’s released.

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
- [protocol PHProjectTypeDescriptionInvalidator](./phprojecttypedescriptioninvalidator.md)
  A protocol that you use to tell the project when and how to invalidate type and footer text.
- [PHProjectInfo.CreationSource](./phprojectinfo/creationsource-swift.enum.md)
  Defines the source of a project extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojecttypedescriptiondatasource)*