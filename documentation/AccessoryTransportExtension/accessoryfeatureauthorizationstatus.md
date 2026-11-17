# AccessoryFeatureAuthorizationStatus

**Framework**: Accessory Transport Extension  
**Kind**: enum  
**Role**: Enumeration

A status that describes whether the system authorizes a feature for an accessory.

**Availability**:
- iOS 27.3+ (Beta)

## Declaration

```swift
enum AccessoryFeatureAuthorizationStatus
```

## Overview

The system returns [`AccessoryFeatureAuthorizationStatus.unknown`](./accessoryfeatureauthorizationstatus/unknown.md) until your app enrolls the feature for the accessory. Subsequent calls return the recorded status.

Read the status with [`authorizationStatus(for:)`](./accessoryworker/authorizationstatus%28for%29.md) or [`authorizationStatus(for:)`](./accessorygpuworker/authorizationstatus%28for%29.md) and enroll the feature with a matching `requestAuthorization(for:)` method.

## Topics

### Determining the authorization status
- [AccessoryFeatureAuthorizationStatus.unknown](./accessoryfeatureauthorizationstatus/unknown.md)
  A value that indicates the system doesn’t have an authorization record for the accessory feature.
- [AccessoryFeatureAuthorizationStatus.unauthorized](./accessoryfeatureauthorizationstatus/unauthorized.md)
  A value that indicates your extension hasn’t authorized the feature.
- [AccessoryFeatureAuthorizationStatus.authorized](./accessoryfeatureauthorizationstatus/authorized.md)
  A value that indicates your extension authorizes the feature.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Checking authorization
- [static func authorizationStatus(for: ASAccessory) async throws -> AccessoryFeatureAuthorizationStatus](./accessorygpuworker/authorizationstatus%28for%29.md)
  Returns the feature’s current authorization status for an accessory.
- [static func requestAuthorization(for: ASAccessory) async throws -> AccessoryFeatureAuthorizationStatus](./accessorygpuworker/requestauthorization%28for%29.md)
  Enrolls the feature for an accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessoryfeatureauthorizationstatus)*