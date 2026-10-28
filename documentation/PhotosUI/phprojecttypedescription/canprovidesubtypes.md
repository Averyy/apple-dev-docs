# canProvideSubtypes

**Framework**: PhotosUI  
**Kind**: property  
**Role**: Instance Property

A Boolean variable indicating whether subtypes can be fetched from the data source.

**Availability**:
- macOS 10.14+

## Declaration

```swift
var canProvideSubtypes: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL canProvideSubtypes;
```

## Discussion

The value is `true` if [`subtypeDescriptions`](./subtypedescriptions.md) is not empty.

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
- [var subtypeDescriptions: [PHProjectTypeDescription]](./subtypedescriptions.md)
  An array of type descriptions used for subtype descriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojecttypedescription/canprovidesubtypes)*