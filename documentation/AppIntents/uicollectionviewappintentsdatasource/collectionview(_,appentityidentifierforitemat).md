# collectionView(_:appEntityIdentifierForItemAt:)

**Framework**: App Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asks the data source to return an app entity identifier for a cell at a particular location in the collection view.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
func collectionView(_ collectionView: UICollectionView, appEntityIdentifierForItemAt indexPath: IndexPath) -> EntityIdentifier?
```

## Return Value

The app entity identifier at the specified location in the collection view.

## Discussion

For more information, refer to [Providing contextual cues to Apple Intelligence and Siri](../providing-contextual-cues-to-apple-intelligence-and-siri.md) and [App Intents](../AppIntents.md).

## Parameters

- `collectionView`: The collection view asking for the app entity identifier.
- `indexPath`: The index path that specifies the section and item number in the collection view.

## Default Implementations

### UICollectionViewAppIntentsDataSource Implementations
- [func collectionView(UICollectionView, appEntityIdentifierForItemAt: IndexPath) -> EntityIdentifier?](./collectionview%28_,appentityidentifierforitemat%29-7mbns.md)
  Asks the data source to return an app entity identifier for a cell at a particular location in the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/uicollectionviewappintentsdatasource/collectionview(_:appentityidentifierforitemat:))*