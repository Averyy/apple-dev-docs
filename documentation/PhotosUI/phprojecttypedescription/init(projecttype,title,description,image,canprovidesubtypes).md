# init(projectType:title:description:image:canProvideSubtypes:)

**Framework**: PhotosUI  
**Kind**: init  
**Role**: Initializer

A designated initializer for project type descriptions with lazily fetched subtypes and a standard description string.

**Availability**:
- macOS 10.14+

## Declaration

```swift
init(projectType: PHProjectType, title localizedTitle: String, description localizedDescription: String?, image: NSImage?, canProvideSubtypes: Bool)
```

```objc
- (instancetype) initWithProjectType:(PHProjectType) projectType title:(NSString *) localizedTitle description:(NSString *) localizedDescription image:(NSImage *) image canProvideSubtypes:(BOOL) canProvideSubtypes;
```

## Parameters

- `projectType`: The type of project being described.
- `localizedTitle`: The localized title of the project type.
- `localizedDescription`: The localized description of the project type.
- `image`: The image associated with the project type in the picker.
- `canProvideSubtypes`: A Boolean variable indicating whether subtypes can be fetched from the data source.

## See Also

### Creating a Project Type Description
- [convenience init(projectType: PHProjectType, title: String, description: String?, image: NSImage?)](./init%28projecttype,title,description,image%29.md)
  A convenience initializer without subtype descriptions.
- [init(projectType: PHProjectType, title: String, description: String?, image: NSImage?, subtypeDescriptions: [PHProjectTypeDescription])](./init%28projecttype,title,description,image,subtypedescriptions%29.md)
  A designated initializer for project type descriptions with the full subtype hierarchy specified up front and a standard string for description text.
- [init(projectType: PHProjectType, title: String, attributedDescription: NSAttributedString?, image: NSImage?, subtypeDescriptions: [PHProjectTypeDescription])](./init%28projecttype,title,attributeddescription,image,subtypedescriptions%29.md)
  A designated initializer for project type descriptions with the full subtype hierarchy specified up front and an attributed string for description text.
- [init(projectType: PHProjectType, title: String, attributedDescription: NSAttributedString?, image: NSImage?, canProvideSubtypes: Bool)](./init%28projecttype,title,attributeddescription,image,canprovidesubtypes%29.md)
  A designated initializer for project type descriptions with lazily fetched subtypes and an attributed description string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojecttypedescription/init(projecttype:title:description:image:canprovidesubtypes:))*