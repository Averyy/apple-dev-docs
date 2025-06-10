# resultCount

**Framework**: Foundation  
**Kind**: property

The number of results returned by the result group.

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
var resultCount: Int { get }
```

#### Discussion

For performance reasons, you should use this property rather than checking the `count` property on [`results`](nsmetadataqueryresultgroup/results.md).

## See Also

- [var attribute: String](nsmetadataqueryresultgroup/attribute.md)
  The result group’s attribute name.
- [var value: Any](nsmetadataqueryresultgroup/value.md)
  The result group’s value.
- [var results: [Any]](nsmetadataqueryresultgroup/results.md)
  An array containing the result group’s result objects.
- [func result(at: Int) -> Any](nsmetadataqueryresultgroup/result(at:).md)
  Returns the query result at a specific index.
- [var subgroups: [NSMetadataQueryResultGroup]?](nsmetadataqueryresultgroup/subgroups.md)
  An array containing the result group’s subgroups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmetadataqueryresultgroup/resultcount)*