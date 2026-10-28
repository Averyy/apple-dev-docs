# HMServiceGroup

**Framework**: HomeKit  
**Kind**: class  
**Role**: Class

A collection of accessory services.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HMServiceGroup
```

```objc
@interface HMServiceGroup : NSObject
```

## Overview

A service group makes it easier to address the services as a single entity. For example, a user might choose to group a set of lights together as “Desk Lamps,” and have another set of lights grouped as “Ceiling Lights”. You create service groups using the [`addServiceGroup(withName:completionHandler:)`](./hmhome/addservicegroup%28withname,completionhandler%29.md) method of [`HMHome`](./hmhome.md). Service groups are visible to Siri and allow users to control a group of services through Siri.

## Topics

### Managing Service Groups
- [var name: String](./hmservicegroup/name.md)
  The name of the service group.
- [var uniqueIdentifier: UUID](./hmservicegroup/uniqueidentifier.md)
  The unique identifier for the service group.
- [func updateName(String, completionHandler: ((any Error)?) -> Void)](./hmservicegroup/updatename%28_,completionhandler%29.md)
  Updates the name of the service group.
- [var services: [HMService]](./hmservicegroup/services.md)
  Array of the services in the service group.
- [func addService(HMService, completionHandler: ((any Error)?) -> Void)](./hmservicegroup/addservice%28_,completionhandler%29.md)
  Adds a new service to the service group.
- [func removeService(HMService, completionHandler: ((any Error)?) -> Void)](./hmservicegroup/removeservice%28_,completionhandler%29.md)
  Removes a service from the service group.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Grouping services
- [func servicesWithTypes([String]) -> [HMService]?](./hmhome/serviceswithtypes%28_%29.md)
  Returns an array of all services provided by accessories in the home that match the specified types.
- [var serviceGroups: [HMServiceGroup]](./hmhome/servicegroups.md)
  An array of all service groups in the home.
- [func addServiceGroup(withName: String, completionHandler: (HMServiceGroup?, (any Error)?) -> Void)](./hmhome/addservicegroup%28withname,completionhandler%29.md)
  Adds a service group to the home.
- [func removeServiceGroup(HMServiceGroup, completionHandler: ((any Error)?) -> Void)](./hmhome/removeservicegroup%28_,completionhandler%29.md)
  Removes a service group from the home.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmservicegroup)*