# content

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array that provides data for the collection view.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var content: [Any] { get set }
```

```objc
@property (copy) NSArray<id> * content;
```

#### Discussion

The content object manages the data in the collection view. Use this object to specify an array of items directly. This property is observable using key-value observing. The collection view also exposes a `content` binding value so that you can specify the array of items using an ArrayController object in Interface Builder.

To specify the data for your collection view, assign a value to this property or to the [`dataSource`](./datasource.md) property, but not both. If you specify a value for the [`dataSource`](./datasource.md) property, the collection view ignores the value in this property.

## See Also

### Configuring the Collection View
- [var delegate: (any NSCollectionViewDelegate)?](./delegate.md)
  The collection view’s delegate object.
- [protocol NSCollectionViewDelegate](../nscollectionviewdelegate.md)
  A set of methods that you use to manage the behavior of a collection view.
- [var backgroundView: NSView?](./backgroundview.md)
  The background view placed behind all items and supplementary views.
- [var backgroundColors: [NSColor]!](./backgroundcolors.md)
  An array containing the collection view’s background colors.
- [var backgroundViewScrollsWithContent: Bool](./backgroundviewscrollswithcontent.md)
  A Boolean value that indicates whether the collection view’s background view scrolls with the items and other content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/content)*