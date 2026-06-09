# StatusAppManagedListManagedConfigurationStateObject

**Framework**: Device Management  
**Kind**: dictionary

The status of any app managed configuration. This key is only present when the managed app has a managed configuration.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 27.0+ (Beta)
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
  The status of any app extension managed configuration. This key’s value is a dictionary whose keys are the bundle identifiers of app extensions that have a managed configuration. The values of each key represent the status of the corresponding app extension’s managed configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusappmanagedlistmanagedconfigurationstateobject)*