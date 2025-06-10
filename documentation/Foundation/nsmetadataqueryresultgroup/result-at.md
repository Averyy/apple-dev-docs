# result(at:)

**Framework**: Foundation  
**Kind**: method

Returns the query result at a specific index.

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
func result(at idx: Int) -> Any
```

#### Return Value

The query result at a specific index.

#### Discussion

For performance reasons, you should use this method when retrieving a specific result, rather than they array contained in [`results`](nsmetadataqueryresultgroup/results.md).

## Parameters

- `idx`: The index of the desired result.

## See Also

- [var attribute: String](nsmetadataqueryresultgroup/attribute.md)
  The result group’s attribute name.
- [var value: Any](nsmetadataqueryresultgroup/value.md)
  The result group’s value.
- [var results: [Any]](nsmetadataqueryresultgroup/results.md)
  An array containing the result group’s result objects.
- [var resultCount: Int](nsmetadataqueryresultgroup/resultcount.md)
  The number of results returned by the result group.
- [var subgroups: [NSMetadataQueryResultGroup]?](nsmetadataqueryresultgroup/subgroups.md)
  An array containing the result group’s subgroups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmetadataqueryresultgroup/result(at:))*