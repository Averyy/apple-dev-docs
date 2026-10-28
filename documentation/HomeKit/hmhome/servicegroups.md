# serviceGroups

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy, readonly) NSArray<HMServiceGroup *> * serviceGroups;
```

## Discussion

Services groups are instances of [`HMServiceGroup`](../hmservicegroup.md).

## See Also

### Grouping services
- [func servicesWithTypes([String]) -> [HMService]?](./serviceswithtypes%28_%29.md)
  Returns an array of all services provided by accessories in the home that match the specified types.
- [func addServiceGroup(withName: String, completionHandler: (HMServiceGroup?, (any Error)?) -> Void)](./addservicegroup%28withname,completionhandler%29.md)
  Adds a service group to the home.
- [func removeServiceGroup(HMServiceGroup, completionHandler: ((any Error)?) -> Void)](./removeservicegroup%28_,completionhandler%29.md)
  Removes a service group from the home.
- [class HMServiceGroup](../hmservicegroup.md)
  A collection of accessory services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/servicegroups)*