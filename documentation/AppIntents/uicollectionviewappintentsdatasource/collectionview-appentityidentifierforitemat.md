# collectionView(_:appEntityIdentifierForItemAt:)

**Framework**: App Intents  
**Kind**: method  
**Required**: Yes

Asks the data source to return an app entity identifier for a cell at a particular location in the collection view.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
func collectionView(_ collectionView: UICollectionView, appEntityIdentifierForItemAt indexPath: IndexPath) -> EntityIdentifier?
```

#### Return Value

The app entity identifier at the specified location in the collection view.

#### Discussion

For more information, refer to doc:Making-onscreen-content-available-to-siri-and-apple-intelligence and [`App Intents`](AppIntents.md).

## Parameters

- `collectionView`: The collection view asking for the app entity identifier.
- `indexPath`: The index path that specifies the section and item number in the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/uicollectionviewappintentsdatasource/collectionview(_:appentityidentifierforitemat:))*