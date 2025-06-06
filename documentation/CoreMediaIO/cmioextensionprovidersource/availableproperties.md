# availableProperties

**Framework**: Core Media I/O  
**Kind**: property  
**Required**: Yes

A set of available properties for a provider.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
var availableProperties: Set<CMIOExtensionProperty> { get }
```

#### Discussion

Don’t change this property value during the life cycle of the associated provider.

## See Also

- [func providerProperties(forProperties: Set<CMIOExtensionProperty>) throws -> CMIOExtensionProviderProperties](cmioextensionprovidersource/providerproperties(forproperties:).md)
  Gets the state of provider properties.
- [func setProviderProperties(CMIOExtensionProviderProperties) throws](cmioextensionprovidersource/setproviderproperties(_:).md)
  Set the state of provider properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionprovidersource/availableproperties)*