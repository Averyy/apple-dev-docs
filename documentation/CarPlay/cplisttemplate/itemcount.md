# itemCount

**Framework**: CarPlay  
**Kind**: property

The total number of items, across all sections, in the list.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var itemCount: Int { get }
```

#### Discussion

This value never exceeds [`maximumItemCount`](cplisttemplate/maximumitemcount.md). If you initialize a list where the total number of items, across all sections, is greater than [`maximumItemCount`](cplisttemplate/maximumitemcount.md), CarPlay only displays items up to this limit and discards the rest.

## See Also

- [class var maximumItemCount: Int](cplisttemplate/maximumitemcount.md)
  The maximum number of items, across all sections, that the template can display.
- [func indexPath(for: any CPListTemplateItem) -> IndexPath?](cplisttemplate/indexpath(for:).md)
  Returns the index path for the specified item.
- [var title: String?](cplisttemplate/title.md)
  The title that the navigation bar displays when the template is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate/itemcount)*