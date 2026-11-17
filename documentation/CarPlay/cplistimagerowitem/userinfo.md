# userInfo

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

App-specific data you associate with the item.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var userInfo: Any? { get set }
```

```objc
@property (nonatomic, strong, nullable) id userInfo;
```

## Discussion

Use this property to attach app-specific data to the row. For example, you might attach the model object from your app that corresponds to the data for the row and its elements. This information is strictly for your app’s usage, and CarPlay doesn’t use it. The default value of this property is `nil`.

## See Also

### Managing the row’s content
- [var text: String?](./text.md)
  The row’s primary text.
- [var elements: [CPListImageRowItemElement]](./elements.md)
  The elements to display in the row.
- [var allowsMultipleLines: Bool](./allowsmultiplelines.md)
  A Boolean value that indicates whether the row displays elements on more than one line.
- [let CPMaximumNumberOfGridImages: Int](../cpmaximumnumberofgridimages.md)
  The maximum number of images that an image row can contain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitem/userinfo)*