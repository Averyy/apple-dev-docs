# image

**Framework**: PhotosUI  
**Kind**: property  
**Role**: Instance Property

An optional image associated with the project type in the picker.

**Availability**:
- macOS 10.13+

## Declaration

```swift
@NSCopying
var image: NSImage? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSImage * image;
```

## Discussion

PNG images with transparent backgrounds are recommended.

## See Also

### Describing a Project Type
- [var projectType: PHProjectType](./projecttype.md)
  An identifier for the project type.
- [var localizedTitle: String](./localizedtitle.md)
  The localized title of the project type as shown to the user.
- [var localizedDescription: String?](./localizeddescription.md)
  The localized description of the project type as shown to the user.
- [var localizedAttributedDescription: NSAttributedString?](./localizedattributeddescription.md)
  The localized attributed description of the project type as shown to the user.
- [var subtypeDescriptions: [PHProjectTypeDescription]](./subtypedescriptions.md)
  An array of type descriptions used for subtype descriptions.
- [var canProvideSubtypes: Bool](./canprovidesubtypes.md)
  A Boolean variable indicating whether subtypes can be fetched from the data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojecttypedescription/image)*