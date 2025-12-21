# invalidateEverything

**Framework**: AppKit  
**Kind**: property

A Boolean that indicates whether all layout data should be marked as invalid.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var invalidateEverything: Bool { get }
```

#### Discussion

The collection view sets this property in response to specific layout invalidation scenarios. For example, the collection view sets the property to [`true`](https://developer.apple.com/documentation/Swift/true) when you change the current layout object, change the data source of the collection view, or call the [`reloadData()`](nscollectionview/reloaddata().md) method and subsequently request a layout invalidation context.

When this property is set to [`true`](https://developer.apple.com/documentation/Swift/true), the layout object must throw away all previous layout information and recompute it.

## See Also

- [var invalidateDataSourceCounts: Bool](nscollectionviewlayoutinvalidationcontext/invalidatedatasourcecounts.md)
  A Boolean that indicates whether the layout object should ask for new section and item counts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayoutinvalidationcontext/invalidateeverything)*