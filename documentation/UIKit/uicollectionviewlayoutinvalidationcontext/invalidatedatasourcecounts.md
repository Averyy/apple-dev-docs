# invalidateDataSourceCounts

**Framework**: UIKit  
**Kind**: property

A Boolean that indicates whether the layout should ask for new section and item counts.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var invalidateDataSourceCounts: Bool { get }
```

#### Discussion

You do not set this property yourself. The collection view sets it in response to specific types of layout invalidation scenarios.  For example, the collection view sets it to [`true`](https://developer.apple.com/documentation/swift/true) when you insert or delete items or call the collection view’s [`reloadData()`](uicollectionview/reloaddata().md) method.

If this property is set to [`true`](https://developer.apple.com/documentation/swift/true), the layout object should query its delegate for the number of sections and items and update its layout based on the new number of items.

## See Also

- [var invalidateEverything: Bool](uicollectionviewlayoutinvalidationcontext/invalidateeverything.md)
  A Boolean that indicates that all layout data should be marked as invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/invalidatedatasourcecounts)*