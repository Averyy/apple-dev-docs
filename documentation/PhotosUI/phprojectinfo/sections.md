# sections

**Framework**: PhotosUI  
**Kind**: property  
**Role**: Instance Property

An array of project sections, each containing one or more section content objects.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var sections: [PHProjectSection] { get }
```

```objc
@property (nonatomic, readonly) NSArray<PHProjectSection *> * sections;
```

## See Also

### Determining Project Type
- [var projectType: PHProjectType](./projecttype.md)
  The project type that the user selected from the project extension options.
- [struct PHProjectType](../phprojecttype.md)
  The type descriptor of a project extension.
- [var creationSource: PHProjectInfo.CreationSource](./creationsource-swift.property.md)
  The source from which the project was created.
- [class PHProjectTypeDescription](../phprojecttypedescription.md)
  An extensible enumerator for [`PHProjectType`](../phprojecttype.md) that’s presented to users in the project picker.
- [protocol PHProjectTypeDescriptionDataSource](../phprojecttypedescriptiondatasource.md)
  A protocol that you use to provide the project with type description data.
- [protocol PHProjectTypeDescriptionInvalidator](../phprojecttypedescriptioninvalidator.md)
  A protocol that you use to tell the project when and how to invalidate type and footer text.
- [PHProjectInfo.CreationSource](./creationsource-swift.enum.md)
  Defines the source of a project extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojectinfo/sections)*