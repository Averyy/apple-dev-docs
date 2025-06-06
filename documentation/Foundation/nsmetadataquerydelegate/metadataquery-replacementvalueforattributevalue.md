# metadataQuery(_:replacementValueForAttribute:value:)

**Framework**: Foundation  
**Kind**: method

Returns a different value for a given attribute and value.

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
optional func metadataQuery(_ query: NSMetadataQuery, replacementValueForAttribute attrName: String, value attrValue: Any) -> Any
```

#### Return Value

Object that replaces the value of `attrName` in the result object

#### Discussion

The delegate implementation of this method could convert specific query attribute values to other attribute values, for example, converting date object values to formatted strings for display.

## Parameters

- `query`: The query that produced the result object with  .
- `attrName`: The attribute in question.
- `attrValue`: The attribute value to replace.

## See Also

- [func metadataQuery(NSMetadataQuery, replacementObjectForResultObject: NSMetadataItem) -> Any](nsmetadataquerydelegate/metadataquery(_:replacementobjectforresultobject:).md)
  Returns a different object for a given query result object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmetadataquerydelegate/metadataquery(_:replacementvalueforattribute:value:))*