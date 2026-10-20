# results

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, readonly) NSArray * results;
```

#### Discussion

The results array is a proxy object that is primarily intended for use with Cocoa bindings. While it is possible to copy the proxy array to get a “snapshot” of the complete current query results, it is generally not recommended due to performance and memory issues. To access individual result array elements you should instead use the [`resultCount`](./resultcount.md) property and the [`result(at:)`](./result%28at%29.md) method.

## See Also

### Getting Query Results
- [var attribute: String](./attribute.md)
  The result group’s attribute name.
- [var value: Any](./value.md)
  The result group’s value.
- [var resultCount: Int](./resultcount.md)
  The number of results returned by the result group.
- [func result(at: Int) -> Any](./result%28at%29.md)
  Returns the query result at a specific index.
- [var subgroups: [NSMetadataQueryResultGroup]?](./subgroups.md)
  An array containing the result group’s subgroups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmetadataqueryresultgroup/results)*