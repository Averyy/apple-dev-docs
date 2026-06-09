# NSTableViewAppIntentsDataSource

**Framework**: App Intents  
**Kind**: protocol

The methods that an object adopts to make items in a table view or outline view discoverable by Apple Intelligence and Siri.

**Availability**:
- macOS 15.4+

## Declaration

```swift
@MainActor
protocol NSTableViewAppIntentsDataSource : AnyObject
```

## Topics

### Instance Methods
- [func outlineView(NSOutlineView, appEntityIdentifierFor: Any?) -> EntityIdentifier?](nstableviewappintentsdatasource/outlineview(_:appentityidentifierfor:).md)
  Asks the data source to return an app entity identifier for a particular item in the outline view.
- [func tableView(NSTableView, appEntityIdentifierFor: Int) -> EntityIdentifier?](nstableviewappintentsdatasource/tableview(_:appentityidentifierfor:).md)
  Asks the data source to return an app entity identifier for a particular row in the table view.

## See Also

- [Providing contextual cues to Apple Intelligence and Siri](providing-contextual-cues-to-apple-intelligence-and-siri.md)
  Annotate your interface with app entities to offer contextual information about your app’s onscreen content.
- [App schema domains](app-schema-domains.md)
  Declare support for well-known actions and content by applying system-defined schemas to your app intents, app entities, and app enumerations.
- [protocol UITableViewAppIntentsDataSource](uitableviewappintentsdatasource.md)
  The methods that an object adopts to make items in a table view discoverable by Apple Intelligence and Siri.
- [protocol UICollectionViewAppIntentsDataSource](uicollectionviewappintentsdatasource.md)
  The methods adopted by the object you use to make items in a collection view discoverable by Apple Intelligence and Siri.
- [protocol NSCollectionViewAppIntentsDataSource](nscollectionviewappintentsdatasource.md)
  The methods adopted by the object you use to make items in a collection view discoverable by Apple Intelligence and Siri.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/nstableviewappintentsdatasource)*