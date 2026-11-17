# indexPath(for:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Returns the index path for the specified item.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func indexPath(for item: any CPListTemplateItem) -> IndexPath?
```

```objc
- (NSIndexPath *) indexPathForItem:(id<CPListTemplateItem>) item;
```

## Return Value

The index path to the item, or `nil` if `item` doesn’t appear in the list. This method configures the [`section`](../../Foundation/nsindexpath/section.md) and [`row`](../../Foundation/nsindexpath/row.md) properties of the returned type with the index and row information.

## Parameters

- `item`: A row in the list.

## See Also

### Getting item details
- [var itemCount: Int](./itemcount.md)
  The total number of items, across all sections, in the list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate/indexpath(for:))*