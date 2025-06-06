# delegate

**Framework**: Foundation  
**Kind**: property

The query’s delegate.

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
unowned(unsafe) var delegate: (any NSMetadataQueryDelegate)? { get set }
```

#### Discussion

This property contains an object that acts as the query’s delegate, or `nil`. The delegate must implement the [`NSMetadataQueryDelegate`](nsmetadataquerydelegate.md). Pass `nil` to remove the current delegate.

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
- [var searchItems: [Any]?](nsmetadataquery/searchitems.md)
  An array of objects that define the query’s scope.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmetadataquery/delegate)*