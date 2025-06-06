# havingPredicate

**Framework**: Core Data  
**Kind**: property

The predicate used to filter rows being returned by a query containing a GROUP BY directive.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var havingPredicate: NSPredicate? { get set }
```

#### Discussion

If a `havingPredicate` value is supplied, the predicate will be run after. Specifying a `havingPredicate` requires that [`propertiesToGroupBy`](nsfetchrequest/propertiestogroupby.md) also be specified.

## See Also

- [class NSFetchRequest](nsfetchrequest.md)
  A description of search criteria used to retrieve data from a persistent store.
- [var propertiesToGroupBy: [Any]?](nsfetchrequest/propertiestogroupby.md)
  An array of objects that indicates how data should be grouped before a select statement is run in a SQL database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchrequest/havingpredicate)*