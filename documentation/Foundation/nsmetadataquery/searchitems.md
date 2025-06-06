# searchItems

**Framework**: Foundation  
**Kind**: property

An array of objects that define the query’s scope.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var searchItems: [Any]? { get set }
```

#### Discussion

Use this method to scope the metadata query to a collection of existing URLs and/or metadata items. This array contains the `NSURL` and/or `NSMetadataItem` items to be searched.

## See Also

- [var searchScopes: [Any]](nsmetadataquery/searchscopes.md)
  An array containing the search scopes.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmetadataquery/searchitems)*