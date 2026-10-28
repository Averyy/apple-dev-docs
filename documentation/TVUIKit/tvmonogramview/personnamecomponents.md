# personNameComponents

**Framework**: TVUIKit  
**Kind**: property  
**Role**: Instance Property

The names used to create a monogram image.

**Availability**:
- tvOS 12.0+ - Deprecated in 27.2 (renamed: __TVMonogramContentConfiguration)

## Declaration

```swift
var personNameComponents: PersonNameComponents? { get set }
```

```objc
@property (nonatomic, strong, nullable) NSPersonNameComponents * personNameComponents;
```

## Discussion

If no image is provided, the monogram object creates an image using the first initial of the [`givenName`](../../Foundation/nspersonnamecomponents/givenname.md) and [`familyName`](../../Foundation/personnamecomponents/familyname.md) attributes contained in this property. The person’s name appears below the monogram image.

## See Also

### Configuring a Monogram
- [var image: UIImage?](./image.md)
  The custom image for the monogram.
- [var title: String?](./title.md)
  The title for the monogram.
- [var subtitle: String?](./subtitle.md)
  The subtitle for the monogram.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvmonogramview/personnamecomponents)*