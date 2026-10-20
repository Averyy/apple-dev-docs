# setProviderProperties(_:)

**Framework**: Core Media I/O  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Set the state of provider properties.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
func setProviderProperties(_ providerProperties: CMIOExtensionProviderProperties) throws
```

```objc
- (BOOL) setProviderProperties:(CMIOExtensionProviderProperties *) providerProperties error:(NSError **) outError;
```

#### Discussion

If you implement this method in Swift and an error occurs, throw an error and pass more detailed information regarding the property or properties that failed in the error that you throw. If you implement this method in Objective-C and an error occurs, pass more detailed information regarding the property or properties that failed in the [`localizedDescription`](../../Foundation/nserror/localizeddescription.md) property of [`NSError`](../../Foundation/nserror.md).

## Parameters

- `providerProperties`: A provider properties object that contains the updated property states.

## See Also

### Configuring Properties
- [var availableProperties: Set<CMIOExtensionProperty>](./availableproperties.md)
  A set of available properties for a provider.
- [func providerProperties(forProperties: Set<CMIOExtensionProperty>) throws -> CMIOExtensionProviderProperties](./providerproperties%28forproperties%29.md)
  Gets the state of provider properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionprovidersource/setproviderproperties(_:))*