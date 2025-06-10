# contentHuggingElements

**Framework**: UIKit  
**Kind**: property

A setting that determines which type of items tightly hug their content.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var contentHuggingElements: UICollectionLayoutListConfiguration.ContentHuggingElements { get set }
```

#### Discussion

The default value of this property is [`supplementaryHeader`](uicollectionlayoutlistconfiguration-swift.struct/contenthuggingelements-swift.struct/supplementaryheader.md) in visionOS, and `[]` on all other platforms.

When the value of this property is [`supplementaryHeader`](uicollectionlayoutlistconfiguration-swift.struct/contenthuggingelements-swift.struct/supplementaryheader.md), header views tightly hug their content. This means header views don’t stretch to fill the width of the collection view if its content’s intrinsic content size is less than the collection view’s width.

## See Also

- [UICollectionLayoutListConfiguration.ContentHuggingElements](uicollectionlayoutlistconfiguration-swift.struct/contenthuggingelements-swift.struct.md)
  Constants that determine which types of items in a collection view tightly hug their content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/contenthuggingelements-swift.property)*