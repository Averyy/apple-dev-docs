# item(at:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Returns the item at the specified index.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func item(at index: Int) -> any CPListTemplateItem
```

```objc
- (id<CPListTemplateItem>) itemAtIndex:(NSUInteger) index;
```

#### Discussion

The index must be within the bounds of the [`items`](./items.md) array, otherwise, your app throws an exception.

## Parameters

- `index`: The item’s index in the section.

## See Also

### Getting Items
- [var items: [any CPListTemplateItem]](./items.md)
  The list of items for the section.
- [func index(of: any CPListTemplateItem) -> Int](./index%28of%29.md)
  Returns the index of the specified item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistsection/item(at:))*