# index(of:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Returns the zero-based index of an item in the section.

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

The zero-based index of the item, or [`NSNotFound`](../../Foundation/nsnotfound-4qp9h.md) if the item isn’t in the section.

## Discussion

Call this method to retrieve the index of an item in the [`items`](./items.md) array.

## Parameters

- `item`: The item to find in the section.

## See Also

### Locating items in the section
- [var items: [any CPListTemplateItem]](./items.md)
  The items in the section.
- [func item(at: Int) -> any CPListTemplateItem](./item%28at%29.md)
  Returns the item at the specified index in the section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistsection/index(of:))*