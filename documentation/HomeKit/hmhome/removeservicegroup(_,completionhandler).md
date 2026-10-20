# removeServiceGroup(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Removes a service group from the home.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func removeServiceGroup(_ group: HMServiceGroup, completionHandler completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func removeServiceGroup(_ group: HMServiceGroup) async throws
```

```objc
- (void) removeServiceGroup:(HMServiceGroup *) group completionHandler:(void (^)(NSError *error)) completion;
```

## Parameters

- `group`: The service group to remove.
- `completion`: The block executed after the request is processed.

  - **error**: `nil` on success; otherwise, error object indicating the reason for failure.

## See Also

### Grouping services
- [func servicesWithTypes([String]) -> [HMService]?](./serviceswithtypes%28_%29.md)
  Returns an array of all services provided by accessories in the home that match the specified types.
- [var serviceGroups: [HMServiceGroup]](./servicegroups.md)
  An array of all service groups in the home.
- [func addServiceGroup(withName: String, completionHandler: (HMServiceGroup?, (any Error)?) -> Void)](./addservicegroup%28withname,completionhandler%29.md)
  Adds a service group to the home.
- [class HMServiceGroup](../hmservicegroup.md)
  A collection of accessory services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/removeservicegroup(_:completionhandler:))*