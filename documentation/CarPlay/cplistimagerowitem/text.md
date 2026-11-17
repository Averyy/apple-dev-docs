# text

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The row’s primary text.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var text: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * text;
```

## Discussion

The row displays this text above the row’s elements.

## See Also

### Managing the row’s content
- [var elements: [CPListImageRowItemElement]](./elements.md)
  The elements to display in the row.
- [var allowsMultipleLines: Bool](./allowsmultiplelines.md)
  A Boolean value that indicates whether the row displays elements on more than one line.
- [var userInfo: Any?](./userinfo.md)
  App-specific data you associate with the item.
- [let CPMaximumNumberOfGridImages: Int](../cpmaximumnumberofgridimages.md)
  The maximum number of images that an image row can contain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitem/text)*