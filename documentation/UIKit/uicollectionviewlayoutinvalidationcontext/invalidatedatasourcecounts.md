# invalidateDataSourceCounts

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the layout should ask for new section and item counts.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var invalidateDataSourceCounts: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL invalidateDataSourceCounts;
```

## Discussion

You do not set this property yourself. The collection view sets it in response to specific types of layout invalidation scenarios.  For example, the collection view sets it to [`true`](../../Swift/true.md) when you insert or delete items or call the collection view’s [`reloadData()`](../uicollectionview/reloaddata%28%29.md) method.

If this property is set to [`true`](../../Swift/true.md), the layout object should query its delegate for the number of sections and items and update its layout based on the new number of items.

## See Also

### Invalidating the Collection View Data
- [var invalidateEverything: Bool](./invalidateeverything.md)
  A Boolean that indicates that all layout data should be marked as invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/invalidatedatasourcecounts)*