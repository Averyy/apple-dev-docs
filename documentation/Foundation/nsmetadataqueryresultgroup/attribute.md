# attribute

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The result group’s attribute name.

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
var attribute: String { get }
```

```objc
@property (copy, readonly) NSString * attribute;
```

## See Also

### Related Documentation
- [File Metadata Search Programming Guide](https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/SpotlightQuery/Concepts/Introduction.html#//apple_ref/doc/uid/TP40001841)
### Getting Query Results
- [var value: Any](./value.md)
  The result group’s value.
- [var results: [Any]](./results.md)
  An array containing the result group’s result objects.
- [var resultCount: Int](./resultcount.md)
  The number of results returned by the result group.
- [func result(at: Int) -> Any](./result%28at%29.md)
  Returns the query result at a specific index.
- [var subgroups: [NSMetadataQueryResultGroup]?](./subgroups.md)
  An array containing the result group’s subgroups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmetadataqueryresultgroup/attribute)*