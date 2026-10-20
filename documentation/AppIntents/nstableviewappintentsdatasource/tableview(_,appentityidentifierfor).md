# tableView(_:appEntityIdentifierFor:)

**Framework**: App Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asks the data source to return an app entity identifier for a particular row in the table view.

**Availability**:
- macOS 15.4+

## Declaration

```swift
@MainActor
func tableView(_ tableView: NSTableView, appEntityIdentifierFor row: Int) -> EntityIdentifier?
```

#### Return Value

The app entity identifier for the item at the specified location in the table view.

## Parameters

- `tableView`: The table-view object asking for the app entity identifier.
- `row`: The row of the item in the table view.

## Default Implementations

### NSTableViewAppIntentsDataSource Implementations
- [func tableView(NSTableView, appEntityIdentifierFor: Int) -> EntityIdentifier?](./tableview%28_,appentityidentifierfor%29-495df.md)
  Asks the data source to return an app entity identifier for a particular row in the table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/nstableviewappintentsdatasource/tableview(_:appentityidentifierfor:))*