# setDeviceProperties(_:)

**Framework**: Core Media I/O  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sets the state of device properties.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
func setDeviceProperties(_ deviceProperties: CMIOExtensionDeviceProperties) throws
```

```objc
- (BOOL) setDeviceProperties:(CMIOExtensionDeviceProperties *) deviceProperties error:(NSError **) outError;
```

## Discussion

If you implement this method in Swift and an error occurs, throw an error and pass more detailed information regarding the property or properties that failed in the error that you throw. If you implement this method in Objective-C and an error occurs, pass more detailed information regarding the property or properties that failed in the [`localizedDescription`](../../Foundation/nserror/localizeddescription.md) property of [`NSError`](../../Foundation/nserror.md).

> **Note**: The property attributes associated with a property state are always `nil` when setting a value.

## Parameters

- `deviceProperties`: A properties object that contains the updated device state.

## See Also

### Managing Properties
- [var availableProperties: Set<CMIOExtensionProperty>](./availableproperties.md)
  A set of available properties that a device provides.
- [func deviceProperties(forProperties: Set<CMIOExtensionProperty>) throws -> CMIOExtensionDeviceProperties](./deviceproperties%28forproperties%29.md)
  Retrieves the state of device properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensiondevicesource/setdeviceproperties(_:))*