# localizedAttributedDescription

**Framework**: PhotosUI  
**Kind**: property  
**Role**: Instance Property

The localized attributed description of the project type as shown to the user.

**Availability**:
- macOS 10.14+

## Declaration

```swift
@NSCopying
var localizedAttributedDescription: NSAttributedString? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSAttributedString * localizedAttributedDescription;
```

#### Discussion

The attributed description is optional. If you don’t provide one, it defaults to the standard nonattributed description.

## See Also

### Describing a Project Type
- [var projectType: PHProjectType](./projecttype.md)
  An identifier for the project type.
- [var localizedTitle: String](./localizedtitle.md)
  The localized title of the project type as shown to the user.
- [var localizedDescription: String?](./localizeddescription.md)
  The localized description of the project type as shown to the user.
- [var image: NSImage?](./image.md)
  An optional image associated with the project type in the picker.
- [var subtypeDescriptions: [PHProjectTypeDescription]](./subtypedescriptions.md)
  An array of type descriptions used for subtype descriptions.
- [var canProvideSubtypes: Bool](./canprovidesubtypes.md)
  A Boolean variable indicating whether subtypes can be fetched from the data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojecttypedescription/localizedattributeddescription)*