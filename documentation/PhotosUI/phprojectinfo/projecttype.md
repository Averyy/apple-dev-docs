# projectType

**Framework**: PhotosUI  
**Kind**: property  
**Role**: Instance Property

The project type that the user selected from the project extension options.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var projectType: PHProjectType { get }
```

```objc
@property (nonatomic, readonly) PHProjectType projectType;
```

#### Discussion

See the [`PHProjectExtensionController`](../phprojectextensioncontroller.md) protocol for more information on configuring the options.

## See Also

### Determining Project Type
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
- [PHProjectInfo.CreationSource](./creationsource-swift.enum.md)
  Defines the source of a project extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojectinfo/projecttype)*