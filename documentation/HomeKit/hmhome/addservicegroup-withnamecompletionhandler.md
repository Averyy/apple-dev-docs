# addServiceGroup(withName:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Adds a service group to the home.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func addServiceGroup(named serviceGroupName: String) async throws -> HMServiceGroup
```

## Parameters

- `serviceGroupName`: The name of the new service group. Must not be  , and must not be the name of a service group already in the home.
- `completion`: The block executed after the request is processed.

## See Also

- [func servicesWithTypes([String]) -> [HMService]?](hmhome/serviceswithtypes(_:).md)
  Returns an array of all services provided by accessories in the home that match the specified types.
- [var serviceGroups: [HMServiceGroup]](hmhome/servicegroups.md)
  An array of all service groups in the home.
- [func removeServiceGroup(HMServiceGroup, completionHandler: ((any Error)?) -> Void)](hmhome/removeservicegroup(_:completionhandler:).md)
  Removes a service group from the home.
- [class HMServiceGroup](hmservicegroup.md)
  A collection of accessory services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/addservicegroup(withname:completionhandler:))*