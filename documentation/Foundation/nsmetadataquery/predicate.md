# predicate

**Framework**: Foundation  
**Kind**: property

The predicate used to filter query results.

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
@NSCopying
var predicate: NSPredicate? { get set }
```

#### Discussion

Setting this property while a query is running stops the query and discards the current results. The receiver immediately starts a new query.

## See Also

- [var searchScopes: [Any]](nsmetadataquery/searchscopes.md)
  An array containing the search scopes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmetadataquery/predicate)*