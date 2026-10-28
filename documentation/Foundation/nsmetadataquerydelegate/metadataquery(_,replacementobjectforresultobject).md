# metadataQuery(_:replacementObjectForResultObject:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (id) metadataQuery:(NSMetadataQuery *) query replacementObjectForResultObject:(NSMetadataItem *) result;
```

## Return Value

Object that replaces the query result object.

## Discussion

By default query result objects are instances of the [`NSMetadataItem`](../nsmetadataitem.md) class. By implementing this method, you can return an object of a different class type for the specified result object.

## Parameters

- `query`: The query that produced the result object to replace.
- `result`: The query result object to replace.

## See Also

### Related Documentation
- [File Metadata Search Programming Guide](https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/SpotlightQuery/Concepts/Introduction.html#//apple_ref/doc/uid/TP40001841)
### Getting Query Results
- [func metadataQuery(NSMetadataQuery, replacementValueForAttribute: String, value: Any) -> Any](./metadataquery%28_,replacementvalueforattribute,value%29.md)
  Returns a different value for a given attribute and value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmetadataquerydelegate/metadataquery(_:replacementobjectforresultobject:))*