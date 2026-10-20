# invalidateEverything

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates that all layout data should be marked as invalid.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var invalidateEverything: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL invalidateEverything;
```

#### Discussion

You do not set this property yourself. The collection view sets it in response to specific types of layout invalidation scenarios. For example, the collection view sets it to [`true`](../../Swift/true.md) when you change the current layout object, change the data source of the collection view, or call the [`reloadData()`](../uicollectionview/reloaddata%28%29.md) method and subsequently request a layout invalidation context.

If this property is set to [`true`](../../Swift/true.md), the layout object should recompute all of its layout-related data.

## See Also

### Invalidating the Collection View Data
- [var invalidateDataSourceCounts: Bool](./invalidatedatasourcecounts.md)
  A Boolean that indicates whether the layout should ask for new section and item counts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/invalidateeverything)*