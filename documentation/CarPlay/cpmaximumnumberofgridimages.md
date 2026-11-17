# CPMaximumNumberOfGridImages

**Framework**: CarPlay  
**Kind**: var  
**Role**: Global Variable

The maximum number of images that an image row can contain.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+

## Declaration

```swift
let CPMaximumNumberOfGridImages: Int
```

```c
extern const NSUInteger CPMaximumNumberOfGridImages;
```

## Discussion

At runtime, use this value to determine the total number of images that CarPlay allows in an image row. The list item may display fewer images, depending on the width of the vehicle’s primary screen.

## See Also

### Managing the row’s content
- [var text: String?](./cplistimagerowitem/text.md)
  The row’s primary text.
- [var elements: [CPListImageRowItemElement]](./cplistimagerowitem/elements.md)
  The elements to display in the row.
- [var allowsMultipleLines: Bool](./cplistimagerowitem/allowsmultiplelines.md)
  A Boolean value that indicates whether the row displays elements on more than one line.
- [var userInfo: Any?](./cplistimagerowitem/userinfo.md)
  App-specific data you associate with the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaximumnumberofgridimages)*