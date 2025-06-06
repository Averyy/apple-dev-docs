# init(query:)

**Framework**: CloudKit  
**Kind**: init

Creates an operation that searches for records in the specified record zone.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
convenience init(query: CKQuery)
```

#### Discussion

You can use the operation that this method returns only once to perform a search, but you can reuse the query that you provide. During execution, the operation performs a new search and returns the first batch of results. If there are more results available, you must create a separate query object using the provided cursor object.

## Parameters

- `query`: The query for the search.

## See Also

- [convenience init(cursor: CKQueryOperation.Cursor)](ckqueryoperation/init(cursor:).md)
  Creates an operation with additional results from a previous search.
- [init()](ckqueryoperation/init.md)
  Creates an empty query operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckqueryoperation/init(query:))*