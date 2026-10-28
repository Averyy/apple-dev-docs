# tableView(_:appEntityIdentifierForRowAt:)

**Framework**: App Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asks the data source to return an app entity identifier for a cell at a particular location in the table view.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
func tableView(_ tableView: UITableView, appEntityIdentifierForRowAt indexPath: IndexPath) -> EntityIdentifier?
```

## Return Value

The app entity identifier for the item at the specified location in the table view.

## Discussion

For more information, refer to [Providing contextual cues to Apple Intelligence and Siri](../providing-contextual-cues-to-apple-intelligence-and-siri.md) and [App Intents](../AppIntents.md).

## Parameters

- `tableView`: The table-view object asking for the app entity identifier.
- `indexPath`: An index path locating a row in the table view.

## Default Implementations

### UITableViewAppIntentsDataSource Implementations
- [func tableView(UITableView, appEntityIdentifierForRowAt: IndexPath) -> EntityIdentifier?](./tableview%28_,appentityidentifierforrowat%29-8jkr9.md)
  Asks the data source to return an app entity identifier for a cell at a particular location in the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/uitableviewappintentsdatasource/tableview(_:appentityidentifierforrowat:))*