# invalidateDataSourceCounts

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the layout object should ask for new section and item counts.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var invalidateDataSourceCounts: Bool { get }
```

```objc
@property (readonly) BOOL invalidateDataSourceCounts;
```

#### Discussion

The collection view sets this property in response to specific layout invalidation scenarios. For example, the collection view sets the property to [`true`](../../Swift/true.md) when you insert or delete items or call the collection view’s [`reloadData()`](../nscollectionview/reloaddata%28%29.md) method.

When this property is set to [`true`](../../Swift/true.md), the layout object must query the data source for the new number of sections and items. IT should also update its layout based on the updated number of sections and items.

## See Also

### Invalidating the Collection View Data
- [var invalidateEverything: Bool](./invalidateeverything.md)
  A Boolean that indicates whether all layout data should be marked as invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayoutinvalidationcontext/invalidatedatasourcecounts)*