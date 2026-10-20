# availableProperties

**Framework**: Core Media I/O  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A set of properties available for the stream.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
var availableProperties: Set<CMIOExtensionProperty> { get }
```

```objc
@property (atomic, copy, readonly) NSSet<NSString *> * availableProperties;
```

## See Also

### Managing Stream Properties
- [func streamProperties(forProperties: Set<CMIOExtensionProperty>) throws -> CMIOExtensionStreamProperties](./streamproperties%28forproperties%29.md)
  Gets the states of specified properties.
- [func setStreamProperties(CMIOExtensionStreamProperties) throws](./setstreamproperties%28_%29.md)
  Sets the property state of a stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamsource/availableproperties)*