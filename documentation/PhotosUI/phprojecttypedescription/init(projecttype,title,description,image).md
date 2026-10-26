# init(projectType:title:description:image:)

**Framework**: PhotosUI  
**Kind**: init  
**Role**: Initializer

A convenience initializer without subtype descriptions.

**Availability**:
- macOS 10.13+

## Declaration

```swift
convenience init(projectType: PHProjectType, title localizedTitle: String, description localizedDescription: String?, image: NSImage?)
```

```objc
- (instancetype) initWithProjectType:(PHProjectType) projectType title:(NSString *) localizedTitle description:(NSString *) localizedDescription image:(NSImage *) image;
```

## Parameters

- `projectType`: The type of project being described.
- `localizedTitle`: The localized title of the project type.
- `localizedDescription`: The localized attributed description of the project type.
- `image`: The image associated with the project type in the picker.

## See Also

### Creating a Project Type Description
- [init(projectType: PHProjectType, title: String, description: String?, image: NSImage?, subtypeDescriptions: [PHProjectTypeDescription])](./init%28projecttype,title,description,image,subtypedescriptions%29.md)
  A designated initializer for project type descriptions with the full subtype hierarchy specified up front and a standard string for description text.
- [init(projectType: PHProjectType, title: String, attributedDescription: NSAttributedString?, image: NSImage?, subtypeDescriptions: [PHProjectTypeDescription])](./init%28projecttype,title,attributeddescription,image,subtypedescriptions%29.md)
  A designated initializer for project type descriptions with the full subtype hierarchy specified up front and an attributed string for description text.
- [init(projectType: PHProjectType, title: String, description: String?, image: NSImage?, canProvideSubtypes: Bool)](./init%28projecttype,title,description,image,canprovidesubtypes%29.md)
  A designated initializer for project type descriptions with lazily fetched subtypes and a standard description string.
- [init(projectType: PHProjectType, title: String, attributedDescription: NSAttributedString?, image: NSImage?, canProvideSubtypes: Bool)](./init%28projecttype,title,attributeddescription,image,canprovidesubtypes%29.md)
  A designated initializer for project type descriptions with lazily fetched subtypes and an attributed description string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojecttypedescription/init(projecttype:title:description:image:))*