# servicesWithTypes(_:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Returns an array of all services provided by accessories in the home that match the specified types.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func servicesWithTypes(_ serviceTypes: [String]) -> [HMService]?
```

```objc
- (NSArray<HMService *> *) servicesWithTypes:(NSArray<NSString *> *) serviceTypes;
```

## Return Value

An array of found services. Returns `nil` if no matching services are found.

## Parameters

- `serviceTypes`: An array of strings that identify service types. See [Accessory Service Types](../accessory-service-types.md) for a list of types.

## See Also

### Grouping services
- [var serviceGroups: [HMServiceGroup]](./servicegroups.md)
  An array of all service groups in the home.
- [func addServiceGroup(withName: String, completionHandler: (HMServiceGroup?, (any Error)?) -> Void)](./addservicegroup%28withname,completionhandler%29.md)
  Adds a service group to the home.
- [func removeServiceGroup(HMServiceGroup, completionHandler: ((any Error)?) -> Void)](./removeservicegroup%28_,completionhandler%29.md)
  Removes a service group from the home.
- [class HMServiceGroup](../hmservicegroup.md)
  A collection of accessory services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/serviceswithtypes(_:))*