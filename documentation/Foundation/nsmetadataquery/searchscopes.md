# searchScopes

**Framework**: Foundation  
**Kind**: property

An array containing the search scopes.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var searchScopes: [Any] { get set }
```

#### Discussion

This array can contain `NSURL` or `NSString` objects that represent file-system directories or the search scopes for the query. For a list of valid search scopes, see [`Metadata Query Search Scopes`](metadata-query-search-scopes.md). An empty array indicates that there is no limitation on where the query searches.

## See Also

- [File Metadata Search Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Carbon/Conceptual/SpotlightQuery/Concepts/Introduction.html#//apple_ref/doc/uid/TP40001841)
- [var predicate: NSPredicate?](nsmetadataquery/predicate.md)
  The predicate used to filter query results.
- [var sortDescriptors: [NSSortDescriptor]](nsmetadataquery/sortdescriptors.md)
  An array of sort descriptor objects.
- [var valueListAttributes: [String]](nsmetadataquery/valuelistattributes.md)
  An array of attributes whose values are gathered by the query.
- [var groupingAttributes: [String]?](nsmetadataquery/groupingattributes.md)
  An array of grouping attributes. (read-only)
- [var notificationBatchingInterval: TimeInterval](nsmetadataquery/notificationbatchinginterval.md)
  The interval at which notification of updated results occurs.
- [var delegate: (any NSMetadataQueryDelegate)?](nsmetadataquery/delegate.md)
  The query’s delegate.
- [var searchItems: [Any]?](nsmetadataquery/searchitems.md)
  An array of objects that define the query’s scope.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmetadataquery/searchscopes)*