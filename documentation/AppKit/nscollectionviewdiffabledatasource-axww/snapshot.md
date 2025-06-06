# snapshot()

**Framework**: AppKit  
**Kind**: method

Returns a representation of the current state of the data in the collection view.

**Availability**:
- macOS 10.15.1+

## Declaration

```swift
func snapshot() -> NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>
```

#### Return Value

A snapshot containing section and item identifiers in the order that they appear in the UI.

## See Also

- [func apply(NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>, animatingDifferences: Bool, completion: (() -> Void)?)](nscollectionviewdiffabledatasource-axww/apply(_:animatingdifferences:completion:).md)
  Updates the UI to reflect the state of the data in the specified snapshot, optionally animating the UI changes and executing a completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdiffabledatasource-axww/snapshot())*