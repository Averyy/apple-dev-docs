# setStreamProperties(_:)

**Framework**: Core Media I/O  
**Kind**: method  
**Required**: Yes

Sets the property state of a stream.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
func setStreamProperties(_ streamProperties: CMIOExtensionStreamProperties) throws
```

## Parameters

- `streamProperties`: A properties object that contains the new property states.

## See Also

- [var availableProperties: Set<CMIOExtensionProperty>](cmioextensionstreamsource/availableproperties.md)
  A set of properties available for the stream.
- [func streamProperties(forProperties: Set<CMIOExtensionProperty>) throws -> CMIOExtensionStreamProperties](cmioextensionstreamsource/streamproperties(forproperties:).md)
  Gets the states of specified properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamsource/setstreamproperties(_:))*