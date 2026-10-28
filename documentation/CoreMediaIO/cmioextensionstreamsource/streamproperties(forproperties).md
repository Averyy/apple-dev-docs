# streamProperties(forProperties:)

**Framework**: Core Media I/O  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Gets the states of specified properties.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
func streamProperties(forProperties properties: Set<CMIOExtensionProperty>) throws -> CMIOExtensionStreamProperties
```

```objc
- (CMIOExtensionStreamProperties *) streamPropertiesForProperties:(NSSet<NSString *> *) properties error:(NSError **) outError;
```

## Return Value

An object that contains the states of the requested properties.

## Parameters

- `properties`: A set of properties with states to retrieve.

## See Also

### Managing Stream Properties
- [var availableProperties: Set<CMIOExtensionProperty>](./availableproperties.md)
  A set of properties available for the stream.
- [func setStreamProperties(CMIOExtensionStreamProperties) throws](./setstreamproperties%28_%29.md)
  Sets the property state of a stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamsource/streamproperties(forproperties:))*