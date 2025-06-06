# serviceGroups

**Framework**: HomeKit  
**Kind**: property

An array of all service groups in the home.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var serviceGroups: [HMServiceGroup] { get }
```

#### Discussion

Services groups are instances of [`HMServiceGroup`](hmservicegroup.md).

## See Also

- [func servicesWithTypes([String]) -> [HMService]?](hmhome/serviceswithtypes(_:).md)
  Returns an array of all services provided by accessories in the home that match the specified types.
- [func addServiceGroup(withName: String, completionHandler: (HMServiceGroup?, (any Error)?) -> Void)](hmhome/addservicegroup(withname:completionhandler:).md)
  Adds a service group to the home.
- [func removeServiceGroup(HMServiceGroup, completionHandler: ((any Error)?) -> Void)](hmhome/removeservicegroup(_:completionhandler:).md)
  Removes a service group from the home.
- [class HMServiceGroup](hmservicegroup.md)
  A collection of accessory services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/servicegroups)*