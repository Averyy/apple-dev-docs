# setProviderProperties(_:)

**Framework**: Core Media I/O  
**Kind**: method  
**Required**: Yes

Set the state of provider properties.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
func setProviderProperties(_ providerProperties: CMIOExtensionProviderProperties) throws
```

#### Discussion

If you implement this method in Swift and an error occurs, throw an error and pass more detailed information regarding the property or properties that failed in the error that you throw. If you implement this method in Objective-C and an error occurs, pass more detailed information regarding the property or properties that failed in the [`localizedDescription`](https://developer.apple.com/documentation/foundation/nserror/1414418-localizeddescription) property of [`NSError`](https://developer.apple.com/documentation/Foundation/NSError).

## Parameters

- `providerProperties`: A provider properties object that contains the updated property states.

## See Also

- [var availableProperties: Set<CMIOExtensionProperty>](cmioextensionprovidersource/availableproperties.md)
  A set of available properties for a provider.
- [func providerProperties(forProperties: Set<CMIOExtensionProperty>) throws -> CMIOExtensionProviderProperties](cmioextensionprovidersource/providerproperties(forproperties:).md)
  Gets the state of provider properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionprovidersource/setproviderproperties(_:))*