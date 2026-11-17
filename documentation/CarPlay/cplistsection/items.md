# items

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The items in the section.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var items: [any CPListTemplateItem] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<id<CPListTemplateItem>> * items;
```

## Discussion

CarPlay displays items in the same order as the array in this property. This property contains only [`CPListItem`](../cplistitem.md), [`CPListImageRowItem`](../cplistimagerowitem.md), and [`CPMessageListItem`](../cpmessagelistitem.md) item types.

## See Also

### Locating items in the section
- [func index(of: any CPListTemplateItem) -> Int](./index%28of%29.md)
  Returns the zero-based index of an item in the section.
- [func item(at: Int) -> any CPListTemplateItem](./item%28at%29.md)
  Returns the item at the specified index in the section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistsection/items)*