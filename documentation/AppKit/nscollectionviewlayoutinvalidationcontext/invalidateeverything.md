# invalidateEverything

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether all layout data should be marked as invalid.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var invalidateEverything: Bool { get }
```

```objc
@property (readonly) BOOL invalidateEverything;
```

## Discussion

The collection view sets this property in response to specific layout invalidation scenarios. For example, the collection view sets the property to [`true`](../../Swift/true.md) when you change the current layout object, change the data source of the collection view, or call the [`reloadData()`](../nscollectionview/reloaddata%28%29.md) method and subsequently request a layout invalidation context.

When this property is set to [`true`](../../Swift/true.md), the layout object must throw away all previous layout information and recompute it.

## See Also

### Invalidating the Collection View Data
- [var invalidateDataSourceCounts: Bool](./invalidatedatasourcecounts.md)
  A Boolean that indicates whether the layout object should ask for new section and item counts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayoutinvalidationcontext/invalidateeverything)*