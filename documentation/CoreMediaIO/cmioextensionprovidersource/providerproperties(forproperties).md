# providerProperties(forProperties:)

**Framework**: Core Media I/O  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Gets the state of provider properties.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
func providerProperties(forProperties properties: Set<CMIOExtensionProperty>) throws -> CMIOExtensionProviderProperties
```

```objc
- (CMIOExtensionProviderProperties *) providerPropertiesForProperties:(NSSet<NSString *> *) properties error:(NSError **) outError;
```

#### Return Value

A provider properties object that contains the state of the requested properties.

## Parameters

- `properties`: A set of properties for which to retrieve the state.

## See Also

### Configuring Properties
- [var availableProperties: Set<CMIOExtensionProperty>](./availableproperties.md)
  A set of available properties for a provider.
- [func setProviderProperties(CMIOExtensionProviderProperties) throws](./setproviderproperties%28_%29.md)
  Set the state of provider properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionprovidersource/providerproperties(forproperties:))*