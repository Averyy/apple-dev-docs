# item(at:)

**Framework**: CarPlay  
**Kind**: method

Returns the item at the specified index.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func item(at index: Int) -> any CPListTemplateItem
```

#### Discussion

The index must be within the bounds of the [`items`](cplistsection/items.md) array, otherwise, your app throws an exception.

## Parameters

- `index`: The item’s index in the section.

## See Also

- [var items: [any CPListTemplateItem]](cplistsection/items.md)
  The list of items for the section.
- [func index(of: any CPListTemplateItem) -> Int](cplistsection/index(of:).md)
  Returns the index of the specified item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistsection/item(at:))*