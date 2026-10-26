# subtypeDescriptions

**Framework**: PhotosUI  
**Kind**: property  
**Role**: Instance Property

An array of type descriptions used for subtype descriptions.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var subtypeDescriptions: [PHProjectTypeDescription] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<PHProjectTypeDescription *> * subtypeDescriptions;
```

#### Discussion

This array may be empty.

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
- [var image: NSImage?](./image.md)
  An optional image associated with the project type in the picker.
- [var canProvideSubtypes: Bool](./canprovidesubtypes.md)
  A Boolean variable indicating whether subtypes can be fetched from the data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojecttypedescription/subtypedescriptions)*