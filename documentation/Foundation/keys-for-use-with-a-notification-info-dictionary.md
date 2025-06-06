# Keys for Use with a Notification Info Dictionary

**Framework**: Foundation

Constants for keys to retrieve the collection of changed items from a notification’s user info dictionary.

#### Overview

When querying the ubiquitous scope, these keys get added to the user info dictionary only in OS X v10.10 and iOS 8.0 or later, and only when iCloud Drive is enabled for the user’s iCloud account. To track changes in earlier versions of the SDK, use KVO on the query’s `results` property instead.

## Topics

### Constants
- [let NSMetadataQueryUpdateAddedItemsKey: String](nsmetadataqueryupdateaddeditemskey.md)
  The key for retrieving an array of items added to the query result. By default, this array contains [`NSMetadataItem`](nsmetadataitem.md) objects, representing the query’s results; however, the query’s delegate can substitute these objects with instances of a different class.
- [let NSMetadataQueryUpdateChangedItemsKey: String](nsmetadataqueryupdatechangeditemskey.md)
  The key for retrieving an array of items that have changed in the query result. By default, this array contains [`NSMetadataItem`](nsmetadataitem.md) objects, representing the query’s results; however, the query’s delegate can substitute these objects with instances of a different class.
- [let NSMetadataQueryUpdateRemovedItemsKey: String](nsmetadataqueryupdateremoveditemskey.md)
  The key for retrieving an array of items removed from the query result. By default, this array contains [`NSMetadataItem`](nsmetadataitem.md) objects, representing the query’s results; however, the query’s delegate can substitute these objects with instances of a different class.

## See Also

- [Metadata Query Search Scopes](metadata-query-search-scopes.md)
  Constants for the predefined search scopes used by [`searchScopes`](nsmetadataquery/searchscopes.md).
- [Content Relevance](content-relevance.md)
  In addition to including the requested metadata attributes, a query result also includes content relevance, accessed with the following key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/keys-for-use-with-a-notification-info-dictionary)*