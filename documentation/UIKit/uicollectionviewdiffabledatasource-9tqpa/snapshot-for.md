# snapshot(for:)

**Framework**: UIKit  
**Kind**: method

Returns a representation of the current state of the data in the specified section of the collection view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func snapshot(for section: SectionIdentifierType) -> NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>
```

## See Also

- [func apply(NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>, to: SectionIdentifierType, animatingDifferences: Bool, completion: (() -> Void)?)](uicollectionviewdiffabledatasource-9tqpa/apply(_:to:animatingdifferences:completion:).md)
  Updates the section UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes and executing a completion handler.
- [func apply(NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>, to: SectionIdentifierType, animatingDifferences: Bool) async](uicollectionviewdiffabledatasource-9tqpa/apply(_:to:animatingdifferences:).md)
  Updates the section UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/snapshot(for:))*