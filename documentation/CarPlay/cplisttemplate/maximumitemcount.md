# maximumItemCount

**Framework**: CarPlay  
**Kind**: property

The maximum number of items, across all sections, that the template can display.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
class var maximumItemCount: Int { get }
```

#### Discussion

This property’s value is dependent on any user interface limits that the vehicle imposes. See [`CPSessionConfiguration`](cpsessionconfiguration.md) for more information. At runtime, use this value to determine the maximum number of items, across all sections, that your list can display.

## See Also

- [var itemCount: Int](cplisttemplate/itemcount.md)
  The total number of items, across all sections, in the list.
- [func indexPath(for: any CPListTemplateItem) -> IndexPath?](cplisttemplate/indexpath(for:).md)
  Returns the index path for the specified item.
- [var title: String?](cplisttemplate/title.md)
  The title that the navigation bar displays when the template is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate/maximumitemcount)*