# tableView(_:appEntityIdentifierForRowAt:)

**Framework**: App Intents  
**Kind**: method  
**Required**: Yes

Asks the data source to return an app entity identifier for a cell at a particular location in the table view.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
func tableView(_ tableView: UITableView, appEntityIdentifierForRowAt indexPath: IndexPath) -> EntityIdentifier?
```

#### Return Value

The app entity identifier for the item at the specified location in the table view.

#### Discussion

For more information, refer to doc:providing-contextual-cues-to-Apple-Intelligence-and-Siri and [`App Intents`](AppIntents.md).

## Parameters

- `tableView`: The table-view object asking for the app entity identifier.
- `indexPath`: An index path locating a row in the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/uitableviewappintentsdatasource/tableview(_:appentityidentifierforrowat:))*