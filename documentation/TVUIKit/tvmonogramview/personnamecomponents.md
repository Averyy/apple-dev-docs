# personNameComponents

**Framework**: TVUIKit  
**Kind**: property

The names used to create a monogram image.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
@MainActor
var personNameComponents: PersonNameComponents? { get set }
```

#### Discussion

If no image is provided, the monogram object creates an image using the first initial of the [`givenName`](https://developer.apple.com/documentation/Foundation/NSPersonNameComponents/givenName) and [`familyName`](https://developer.apple.com/documentation/Foundation/PersonNameComponents/familyName) attributes contained in this property. The person’s name appears below the monogram image.

## See Also

- [var image: UIImage?](tvmonogramview/image.md)
  The custom image for the monogram.
- [var title: String?](tvmonogramview/title.md)
  The title for the monogram.
- [var subtitle: String?](tvmonogramview/subtitle.md)
  The subtitle for the monogram.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvmonogramview/personnamecomponents)*