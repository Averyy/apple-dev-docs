# items

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The list of items for the section.

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

## See Also

### Getting Items
- [func index(of: any CPListTemplateItem) -> Int](./index%28of%29.md)
  Returns the index of the specified item.
- [func item(at: Int) -> any CPListTemplateItem](./item%28at%29.md)
  Returns the item at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistsection/items)*