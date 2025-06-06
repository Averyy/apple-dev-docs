# apply(_:to:animatingDifferences:)

**Framework**: UIKit  
**Kind**: method

Updates the section UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- tvOS 15.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func apply(_ snapshot: NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>, to section: SectionIdentifierType, animatingDifferences: Bool = true) async
```

## See Also

- [func snapshot(for: SectionIdentifierType) -> NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>](uicollectionviewdiffabledatasource-9tqpa/snapshot(for:).md)
  Returns a representation of the current state of the data in the specified section of the collection view.
- [func apply(NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>, to: SectionIdentifierType, animatingDifferences: Bool, completion: (() -> Void)?)](uicollectionviewdiffabledatasource-9tqpa/apply(_:to:animatingdifferences:completion:).md)
  Updates the section UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes and executing a completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/apply(_:to:animatingdifferences:))*