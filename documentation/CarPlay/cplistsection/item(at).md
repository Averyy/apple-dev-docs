# item(at:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Returns the item at the specified index in the section.

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

## Return Value

The item at the specified index.

## Parameters

- `index`: The item’s zero-based index in the section. If you specify an index outside of the bounds of the [`items`](./items.md) array, this method raises an exception.

## See Also

### Locating items in the section
- [var items: [any CPListTemplateItem]](./items.md)
  The items in the section.
- [func index(of: any CPListTemplateItem) -> Int](./index%28of%29.md)
  Returns the zero-based index of an item in the section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistsection/item(at:))*