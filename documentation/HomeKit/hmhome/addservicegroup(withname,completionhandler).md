# addServiceGroup(withName:completionHandler:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Adds a service group to the home.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func addServiceGroup(withName serviceGroupName: String, completionHandler completion: @escaping @Sendable (HMServiceGroup?, (any Error)?) -> Void)
```

```swift
func addServiceGroup(named serviceGroupName: String) async throws -> HMServiceGroup
```

```objc
- (void) addServiceGroupWithName:(NSString *) serviceGroupName completionHandler:(void (^)(HMServiceGroup *group, NSError *error)) completion;
```

## Parameters

- `serviceGroupName`: The name of the new service group. Must not be `nil`, and must not be the name of a service group already in the home.
- `completion`: The block executed after the request is processed.

  - **group**: The newly created service group.
  - **error**: `nil` on success; otherwise, error object indicating the reason for failure.

## See Also

### Grouping services
- [func servicesWithTypes([String]) -> [HMService]?](./serviceswithtypes%28_%29.md)
  Returns an array of all services provided by accessories in the home that match the specified types.
- [var serviceGroups: [HMServiceGroup]](./servicegroups.md)
  An array of all service groups in the home.
- [func removeServiceGroup(HMServiceGroup, completionHandler: ((any Error)?) -> Void)](./removeservicegroup%28_,completionhandler%29.md)
  Removes a service group from the home.
- [class HMServiceGroup](../hmservicegroup.md)
  A collection of accessory services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/addservicegroup(withname:completionhandler:))*