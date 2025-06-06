# indexPath(for:)

**Framework**: CarPlay  
**Kind**: method

Returns the index path for the specified item.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func indexPath(for item: any CPListTemplateItem) -> IndexPath?
```

#### Return Value

The item’s index path in the list, or [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0) if the list doesn’t contain the item.

## Parameters

- `item`: The item to find in the list.

## See Also

- [class var maximumItemCount: Int](cplisttemplate/maximumitemcount.md)
  The maximum number of items, across all sections, that the template can display.
- [var itemCount: Int](cplisttemplate/itemcount.md)
  The total number of items, across all sections, in the list.
- [var title: String?](cplisttemplate/title.md)
  The title that the navigation bar displays when the template is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate/indexpath(for:))*