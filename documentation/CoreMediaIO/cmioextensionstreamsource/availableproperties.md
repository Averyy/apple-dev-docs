# availableProperties

**Framework**: Core Media I/O  
**Kind**: property  
**Required**: Yes

A set of properties available for the stream.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
var availableProperties: Set<CMIOExtensionProperty> { get }
```

## See Also

- [func streamProperties(forProperties: Set<CMIOExtensionProperty>) throws -> CMIOExtensionStreamProperties](cmioextensionstreamsource/streamproperties(forproperties:).md)
  Gets the states of specified properties.
- [func setStreamProperties(CMIOExtensionStreamProperties) throws](cmioextensionstreamsource/setstreamproperties(_:).md)
  Sets the property state of a stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamsource/availableproperties)*