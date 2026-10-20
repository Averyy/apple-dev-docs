# availableProperties

**Framework**: Core Media I/O  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A set of available properties for a provider.

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

#### Discussion

Don’t change this property value during the life cycle of the associated provider.

## See Also

### Configuring Properties
- [func providerProperties(forProperties: Set<CMIOExtensionProperty>) throws -> CMIOExtensionProviderProperties](./providerproperties%28forproperties%29.md)
  Gets the state of provider properties.
- [func setProviderProperties(CMIOExtensionProviderProperties) throws](./setproviderproperties%28_%29.md)
  Set the state of provider properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionprovidersource/availableproperties)*