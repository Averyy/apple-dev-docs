# elements

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The elements to display in the row.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var elements: [CPListImageRowItemElement] { get set }
```

```objc
@property (nonatomic, copy) NSArray<CPListImageRowItemElement *> * elements;
```

## Discussion

This property contains the elements you provided at initialization time. The type of the elements in this array depends on the initializer you used when you created the [`CPListImageRowItem`](../cplistimagerowitem.md) object.

To change the elements in the array, assign an updated value to this property. Make sure every element in the new array has the same type. If your array contains multiple element types, CarPlay chooses the first element type it finds and discards elements of other types. After you assign the new value, CarPlay refreshes the appearance of your list interface.

## See Also

### Managing the row’s content
- [var text: String?](./text.md)
  The row’s primary text.
- [var allowsMultipleLines: Bool](./allowsmultiplelines.md)
  A Boolean value that indicates whether the row displays elements on more than one line.
- [var userInfo: Any?](./userinfo.md)
  App-specific data you associate with the item.
- [let CPMaximumNumberOfGridImages: Int](../cpmaximumnumberofgridimages.md)
  The maximum number of images that an image row can contain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitem/elements)*