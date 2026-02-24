# StatusAppManagedListManagedConfigurationStateObject

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that contains details about a declarative managed app’s managed configuration.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- visionOS 2.4+

## Declaration

```swift
object StatusAppManagedListManagedConfigurationStateObject
```

## Properties

- `state` (string) *(required)*: The managed configuration status. - `unknown`: The managed configuration has not been read
- `invalid`: The managed configuration was read and deemed to be invalid
- `valid`: The managed configuration was read and deemed to be valid

## See Also

- [object StatusAppManagedListManagedConfiguration_ExtensionConfigStateObject](statusappmanagedlistmanagedconfiguration_extensionconfigstateobject.md)
  A dictionary that contains details about a declarative managed app extension’s managed configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusappmanagedlistmanagedconfigurationstateobject)*