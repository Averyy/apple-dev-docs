# NSMetadataQueryDelegate

**Framework**: Foundation  
**Kind**: protocol

An interface that enables the delegate of a metadata query to provide substitute results or attributes.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
protocol NSMetadataQueryDelegate : NSObjectProtocol
```

## Topics

### Getting Query Results
- [func metadataQuery(NSMetadataQuery, replacementObjectForResultObject: NSMetadataItem) -> Any](nsmetadataquerydelegate/metadataquery(_:replacementobjectforresultobject:).md)
  Returns a different object for a given query result object.
- [func metadataQuery(NSMetadataQuery, replacementValueForAttribute: String, value: Any) -> Any](nsmetadataquerydelegate/metadataquery(_:replacementvalueforattribute:value:).md)
  Returns a different value for a given attribute and value.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSMetadataQuery](nsmetadataquery.md)
  A query that you perform against Spotlight metadata.
- [class NSMetadataItem](nsmetadataitem.md)
  The metadata associated with a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmetadataquerydelegate)*