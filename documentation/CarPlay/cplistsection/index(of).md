# index(of:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Returns the index of the specified item.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func index(of item: any CPListTemplateItem) -> Int
```

```objc
- (NSUInteger) indexOfItem:(id<CPListTemplateItem>) item;
```

## Return Value

The item’s index in the section, or [`NSNotFound`](../../Foundation/nsnotfound-4qp9h.md) if the section doesn’t contain the item.

## Parameters

- `item`: The item to find in the section.

## See Also

### Getting Items
- [var items: [any CPListTemplateItem]](./items.md)
  The list of items for the section.
- [func item(at: Int) -> any CPListTemplateItem](./item%28at%29.md)
  Returns the item at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistsection/index(of:))*