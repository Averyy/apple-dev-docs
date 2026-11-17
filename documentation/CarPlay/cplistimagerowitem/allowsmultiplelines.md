# allowsMultipleLines

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the row displays elements on more than one line.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var allowsMultipleLines: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL allowsMultipleLines;
```

## Discussion

When the value of this property is `true`, CarPlay adds extra lines until it displays all the elements. When the value of this property is `false`, CarPlay displays only a single line of elements. If there isn’t enough room to display all of the elements in a single line, CarPlay displays only as many elements as fit and ignores the rest.

## See Also

### Managing the row’s content
- [var text: String?](./text.md)
  The row’s primary text.
- [var elements: [CPListImageRowItemElement]](./elements.md)
  The elements to display in the row.
- [var userInfo: Any?](./userinfo.md)
  App-specific data you associate with the item.
- [let CPMaximumNumberOfGridImages: Int](../cpmaximumnumberofgridimages.md)
  The maximum number of images that an image row can contain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitem/allowsmultiplelines)*