# index(of:)

**Framework**: CarPlay  
**Kind**: method

Returns the index of the specified item.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func index(of item: any CPListTemplateItem) -> Int
```

#### Return Value

The item’s index in the section, or [`NSNotFound`](https://developer.apple.com/documentation/Foundation/NSNotFound-4qp9h) if the section doesn’t contain the item.

## Parameters

- `item`: The item to find in the section.

## See Also

- [var items: [any CPListTemplateItem]](cplistsection/items.md)
  The list of items for the section.
- [func item(at: Int) -> any CPListTemplateItem](cplistsection/item(at:).md)
  Returns the item at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistsection/index(of:))*