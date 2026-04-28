# StatusAppManagedListManagedConfigurationObject

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that contains details about a declarative managed app’s managed configuration.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- visionOS 2.4+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object StatusAppManagedListManagedConfigurationObject
```

## Topics

### Objects
- [object StatusAppManagedListManagedConfigurationStateObject](statusappmanagedlistmanagedconfigurationstateobject.md)
  A dictionary that contains details about a declarative managed app’s managed configuration.
- [object StatusAppManagedListManagedConfiguration_ExtensionConfigStateObject](statusappmanagedlistmanagedconfiguration_extensionconfigstateobject.md)
  A dictionary that contains details about a declarative managed app extension’s managed configuration.

## Properties

- `app-config-state` (StatusAppManagedListManagedConfigurationStateObject): The status of any app managed configuration. This key is only present when the managed app has a managed configuration.
- `extension-config-state` (StatusAppManagedListManagedConfiguration_ExtensionConfigStateObject): The status of any app extension managed configuration. This key’s value is a dictionary whose keys are the bundle identifiers of app extensions that have a managed configuration. The values of each key represent the status of the corresponding app extension’s managed configuration.

## See Also

- [object StatusAppManagedListStatusReasonObject](statusappmanagedliststatusreasonobject.md)
  A dictionary that contains details about a declarative managed app’s state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusappmanagedlistmanagedconfigurationobject)*