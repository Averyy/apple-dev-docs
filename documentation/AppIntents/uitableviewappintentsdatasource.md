# UITableViewAppIntentsDataSource

**Framework**: App Intents  
**Kind**: protocol

The methods that an object adopts to make items in a table view discoverable by Apple Intelligence and Siri.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
protocol UITableViewAppIntentsDataSource : AnyObject
```

#### Overview

For more information, refer to doc:providing-contextual-cues-to-Apple-Intelligence-and-Siri and [`App Intents`](AppIntents.md).

## Topics

### Instance Methods
- [func tableView(UITableView, appEntityIdentifierForRowAt: IndexPath) -> EntityIdentifier?](uitableviewappintentsdatasource/tableview(_:appentityidentifierforrowat:).md)
  Asks the data source to return an app entity identifier for a cell at a particular location in the table view.

## See Also

- [Providing contextual cues to Apple Intelligence and Siri](providing-contextual-cues-to-apple-intelligence-and-siri.md)
  Annotate your interface with app entities to offer contextual information about your app’s onscreen content.
- [App schema domains](app-schema-domains.md)
  Declare support for well-known actions and content by applying system-defined schemas to your app intents, app entities, and app enumerations.
- [protocol NSTableViewAppIntentsDataSource](nstableviewappintentsdatasource.md)
  The methods that an object adopts to make items in a table view or outline view discoverable by Apple Intelligence and Siri.
- [protocol UICollectionViewAppIntentsDataSource](uicollectionviewappintentsdatasource.md)
  The methods adopted by the object you use to make items in a collection view discoverable by Apple Intelligence and Siri.
- [protocol NSCollectionViewAppIntentsDataSource](nscollectionviewappintentsdatasource.md)
  The methods adopted by the object you use to make items in a collection view discoverable by Apple Intelligence and Siri.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/uitableviewappintentsdatasource)*