# metadataQuery(_:replacementObjectForResultObject:)

**Framework**: Foundation  
**Kind**: method

Returns a different object for a given query result object.

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
optional func metadataQuery(_ query: NSMetadataQuery, replacementObjectForResultObject result: NSMetadataItem) -> Any
```

#### Return Value

Object that replaces the query result object.

#### Discussion

By default query result objects are instances of the [`NSMetadataItem`](nsmetadataitem.md) class. By implementing this method, you can return an object of a different class type for the specified result object.

## Parameters

- `query`: The query that produced the result object to replace.
- `result`: The query result object to replace.

## See Also

- [File Metadata Search Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Carbon/Conceptual/SpotlightQuery/Concepts/Introduction.html#//apple_ref/doc/uid/TP40001841)
- [func metadataQuery(NSMetadataQuery, replacementValueForAttribute: String, value: Any) -> Any](nsmetadataquerydelegate/metadataquery(_:replacementvalueforattribute:value:).md)
  Returns a different value for a given attribute and value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmetadataquerydelegate/metadataquery(_:replacementobjectforresultobject:))*