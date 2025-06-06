# init(cursor:)

**Framework**: CloudKit  
**Kind**: init

Creates an operation with additional results from a previous search.

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
convenience init(cursor: CKQueryOperation.Cursor)
```

#### Discussion

Use this method to create an operation that retrieves the next batch of results from a previous search. When executing searches for a cursor, don’t cache cursors for a long time before using them. A cursor isn’t a snapshot of the previous search results; it stores a relative offset into the results list. An operation that you create from a cursor performs a new search, sorts the new set of results, and uses the previous offset value to determine where the next batch of results starts.

## Parameters

- `cursor`: The cursor that identifies the previous search. CloudKit passes this value to the completion handler of the previous search. For more information, see the   property.

## See Also

- [convenience init(query: CKQuery)](ckqueryoperation/init(query:).md)
  Creates an operation that searches for records in the specified record zone.
- [init()](ckqueryoperation/init.md)
  Creates an empty query operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckqueryoperation/init(cursor:))*