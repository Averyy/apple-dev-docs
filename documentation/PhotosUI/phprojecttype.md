# PHProjectType

**Framework**: PhotosUI  
**Kind**: struct  
**Role**: Structure

The type descriptor of a project extension.

**Availability**:
- macOS

## Declaration

```swift
struct PHProjectType
```

```c
typedef NSString * PHProjectType;
```

## Topics

### Initializing a Project Type
- [init(String)](./phprojecttype/init%28_%29.md)
  Initializes a project type from a string.
- [init(rawValue: String)](./phprojecttype/init%28rawvalue%29.md)
  Initializes a project type from its raw string value.
### Defining a Project Type
- [static let undefined: PHProjectType](./phprojecttype/undefined.md)
  An undefined project type.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Determining Project Type
- [var projectType: PHProjectType](./phprojectinfo/projecttype.md)
  The project type that the user selected from the project extension options.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojecttype)*