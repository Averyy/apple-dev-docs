# image

**Framework**: TVUIKit  
**Kind**: property  
**Role**: Instance Property

The custom image for the monogram.

**Availability**:
- tvOS 12.0+ - Deprecated in 27.2 (renamed: __TVMonogramContentConfiguration)

## Declaration

```swift
var image: UIImage? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIImage * image;
```

#### Discussion

If you supply an image, the system uses this image instead of a generic image or an image created from the name components.

## See Also

### Configuring a Monogram
- [var personNameComponents: PersonNameComponents?](./personnamecomponents.md)
  The names used to create a monogram image.
- [var title: String?](./title.md)
  The title for the monogram.
- [var subtitle: String?](./subtitle.md)
  The subtitle for the monogram.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvmonogramview/image)*