# removeServiceGroup(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Removes a service group from the home.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func removeServiceGroup(_ group: HMServiceGroup) async throws
```

## Parameters

- `group`: The service group to remove.
- `completion`: The block executed after the request is processed.

## See Also

- [func servicesWithTypes([String]) -> [HMService]?](hmhome/serviceswithtypes(_:).md)
  Returns an array of all services provided by accessories in the home that match the specified types.
- [var serviceGroups: [HMServiceGroup]](hmhome/servicegroups.md)
  An array of all service groups in the home.
- [func addServiceGroup(withName: String, completionHandler: (HMServiceGroup?, (any Error)?) -> Void)](hmhome/addservicegroup(withname:completionhandler:).md)
  Adds a service group to the home.
- [class HMServiceGroup](hmservicegroup.md)
  A collection of accessory services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/removeservicegroup(_:completionhandler:))*