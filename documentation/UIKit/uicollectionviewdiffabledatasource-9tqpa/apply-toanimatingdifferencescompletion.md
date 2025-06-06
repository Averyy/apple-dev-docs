# apply(_:to:animatingDifferences:completion:)

**Framework**: UIKit  
**Kind**: method

Updates the section UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes and executing a completion handler.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func apply(_ snapshot: NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>, to section: SectionIdentifierType, animatingDifferences: Bool = true, completion: (() -> Void)? = nil)
```

## See Also

- [func snapshot(for: SectionIdentifierType) -> NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>](uicollectionviewdiffabledatasource-9tqpa/snapshot(for:).md)
  Returns a representation of the current state of the data in the specified section of the collection view.
- [func apply(NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>, to: SectionIdentifierType, animatingDifferences: Bool) async](uicollectionviewdiffabledatasource-9tqpa/apply(_:to:animatingdifferences:).md)
  Updates the section UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/apply(_:to:animatingdifferences:completion:))*