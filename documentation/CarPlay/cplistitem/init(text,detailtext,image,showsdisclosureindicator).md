# init(text:detailText:image:showsDisclosureIndicator:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Initialize a list item with text, detailtext, an image, and a disclosure indicator.

**Availability**:
- iOS 12.0+ - Deprecated in 14.0
- iPadOS 12.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0

## Declaration

```swift
init(text: String?, detailText: String?, image: UIImage?, showsDisclosureIndicator: Bool)
```

```objc
- (instancetype) initWithText:(NSString *) text detailText:(NSString *) detailText image:(UIImage *) image showsDisclosureIndicator:(BOOL) showsDisclosureIndicator;
```

## Discussion

> **Note**: The maximum size of the image is given by +[CPListItem maximumImageSize].

To properly size your list images, your app should size them to the display scale of the car screen. See -[CPInterfaceController carTraitCollection].

## See Also

### Deprecated
- [var showsDisclosureIndicator: Bool](./showsdisclosureindicator.md)
  If YES, a cell displaying this list item will render with a disclosure indicator in the trailing side of the cell.
- [var showsExplicitLabel: Bool](./showsexplicitlabel.md)
  If YES, a cell displaying this list item will render with an explicit label to the trailing edge of the text


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitem/init(text:detailtext:image:showsdisclosureindicator:))*