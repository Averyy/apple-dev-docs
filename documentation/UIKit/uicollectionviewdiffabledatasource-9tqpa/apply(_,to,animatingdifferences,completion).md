# apply(_:to:animatingDifferences:completion:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Updates the section UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes and executing a completion handler.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency func apply(_ snapshot: NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>, to section: SectionIdentifierType, animatingDifferences: Bool = true, completion: (() -> Void)? = nil)
```

Available when `SectionIdentifierType` conforms to `Hashable`, `SectionIdentifierType` conforms to `Sendable`, `ItemIdentifierType` conforms to `Hashable`, and `ItemIdentifierType` conforms to `Sendable`.

## See Also

### Updating section data
- [func snapshot(for: SectionIdentifierType) -> NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>](./snapshot%28for%29.md)
  Returns a representation of the current state of the data in the specified section of the collection view.
- [func apply(NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>, to: SectionIdentifierType, animatingDifferences: Bool) async](./apply%28_,to,animatingdifferences%29.md)
  Updates the section UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/apply(_:to:animatingdifferences:completion:))*