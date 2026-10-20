# predicate

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, nullable) NSPredicate * predicate;
```

#### Discussion

Setting this property while a query is running stops the query and discards the current results. The receiver immediately starts a new query.

## See Also

### Configuring queries
- [var searchScopes: [Any]](./searchscopes.md)
  An array containing the search scopes.
- [var sortDescriptors: [NSSortDescriptor]](./sortdescriptors.md)
  An array of sort descriptor objects.
- [var valueListAttributes: [String]](./valuelistattributes.md)
  An array of attributes whose values are gathered by the query.
- [var groupingAttributes: [String]?](./groupingattributes.md)
  An array of grouping attributes. (read-only)
- [var notificationBatchingInterval: TimeInterval](./notificationbatchinginterval.md)
  The interval at which notification of updated results occurs.
- [var delegate: (any NSMetadataQueryDelegate)?](./delegate.md)
  The query’s delegate.
- [var searchItems: [Any]?](./searchitems.md)
  An array of objects that define the query’s scope.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmetadataquery/predicate)*