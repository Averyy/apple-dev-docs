# projectType

**Framework**: PhotosUI  
**Kind**: property  
**Role**: Instance Property

An identifier for the project type.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var projectType: PHProjectType { get }
```

```objc
@property (nonatomic, copy, readonly) PHProjectType projectType;
```

#### Discussion

Add these identifiers to [`PHProjectType`](../phprojecttype.md), the extensible string enumeration.

## See Also

### Describing a Project Type
- [var localizedTitle: String](./localizedtitle.md)
  The localized title of the project type as shown to the user.
- [var localizedDescription: String?](./localizeddescription.md)
  The localized description of the project type as shown to the user.
- [var localizedAttributedDescription: NSAttributedString?](./localizedattributeddescription.md)
  The localized attributed description of the project type as shown to the user.
- [var image: NSImage?](./image.md)
  An optional image associated with the project type in the picker.
- [var subtypeDescriptions: [PHProjectTypeDescription]](./subtypedescriptions.md)
  An array of type descriptions used for subtype descriptions.
- [var canProvideSubtypes: Bool](./canprovidesubtypes.md)
  A Boolean variable indicating whether subtypes can be fetched from the data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojecttypedescription/projecttype)*