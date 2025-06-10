# results

**Framework**: Foundation  
**Kind**: property

An array containing the result group’s result objects.

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
var results: [Any] { get }
```

#### Discussion

The results array is a proxy object that is primarily intended for use with Cocoa bindings. While it is possible to copy the proxy array to get a “snapshot” of the complete current query results, it is generally not recommended due to performance and memory issues. To access individual result array elements you should instead use the [`resultCount`](nsmetadataqueryresultgroup/resultcount.md) property and the [`result(at:)`](nsmetadataqueryresultgroup/result(at:).md) method.

## See Also

- [var attribute: String](nsmetadataqueryresultgroup/attribute.md)
  The result group’s attribute name.
- [var value: Any](nsmetadataqueryresultgroup/value.md)
  The result group’s value.
- [var resultCount: Int](nsmetadataqueryresultgroup/resultcount.md)
  The number of results returned by the result group.
- [func result(at: Int) -> Any](nsmetadataqueryresultgroup/result(at:).md)
  Returns the query result at a specific index.
- [var subgroups: [NSMetadataQueryResultGroup]?](nsmetadataqueryresultgroup/subgroups.md)
  An array containing the result group’s subgroups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmetadataqueryresultgroup/results)*