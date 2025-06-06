# streamProperties(forProperties:)

**Framework**: Core Media I/O  
**Kind**: method  
**Required**: Yes

Gets the states of specified properties.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
func streamProperties(forProperties properties: Set<CMIOExtensionProperty>) throws -> CMIOExtensionStreamProperties
```

#### Return Value

An object that contains the states of the requested properties.

## Parameters

- `properties`: A set of properties with states to retrieve.

## See Also

- [var availableProperties: Set<CMIOExtensionProperty>](cmioextensionstreamsource/availableproperties.md)
  A set of properties available for the stream.
- [func setStreamProperties(CMIOExtensionStreamProperties) throws](cmioextensionstreamsource/setstreamproperties(_:).md)
  Sets the property state of a stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamsource/streamproperties(forproperties:))*