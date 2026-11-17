# AccessoryWorker

**Framework**: Accessory Transport Extension  
**Kind**: struct  
**Role**: Structure

A feature that carries data between your data provider and transport extensions.

**Availability**:
- iOS 27.3+ (Beta)

## Declaration

```swift
struct AccessoryWorker
```

## Mentions

- [Sending data to an accessory in the background](./sending-data-to-an-accessory-in-the-background.md)

## Overview

An *accessory worker* exchanges information with your accessory in the background, without waiting for a person to open your app. Create an instance of this structure in the `extensionPoint` of your [`AccessoryDataProvider`](./accessorydataprovider.md) extension, and open sessions from your transport extension with [`makeFeatureSession(_:)`](./accessorytransportsession/makefeaturesession%28_%29.md) in response to events from your accessory. Your app defines the data format, and the Accessory Transport Extension framework treats the data as opaque, with no additional encryption. Enroll the feature for each accessory with [`requestAuthorization(for:)`](./accessoryworker/requestauthorization%28for%29.md). For more information, see [Sending data to an accessory in the background](./sending-data-to-an-accessory-in-the-background.md).

## Topics

### Handling data-provider sessions
- [AccessoryWorker.Handler](./accessoryworker/handler.md)
  A handler type for the session’s data provider.
- [AccessoryWorker.Session](./accessoryworker/session.md)
  A class that represents the data provider within a session.
### Handling transport-extension sessions
- [AccessoryWorker.FeatureSession](./accessoryworker/featuresession.md)
  A class that represents the session’s transport extension.
### Checking authorization
- [static func authorizationStatus(for: ASAccessory) async throws -> AccessoryFeatureAuthorizationStatus](./accessoryworker/authorizationstatus%28for%29.md)
  Returns the feature’s current authorization status for an accessory.
- [static func requestAuthorization(for: ASAccessory) async throws -> AccessoryFeatureAuthorizationStatus](./accessoryworker/requestauthorization%28for%29.md)
  Enrolls the feature for an accessory.
- [enum AccessoryFeatureAuthorizationStatus](./accessoryfeatureauthorizationstatus.md)
  A status that describes whether the system authorizes a feature for an accessory.
### Creating the feature
- [init(() -> any AccessoryFeatureSessionHandler<AccessoryWorker.Session>)](./accessoryworker/init%28_%29.md)
  Initializes a worker feature with a handler factory.

## Relationships

### Conforms To
- [AccessoryFeature](./accessoryfeature.md)
- [AppExtensionPoint.Capability](../ExtensionFoundation/appextensionpoint/capability.md)
- [Identifiable](../Swift/identifiable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Background work
- [Sending data to an accessory in the background](./sending-data-to-an-accessory-in-the-background.md)
  Move data between your accessory and your app when a person’s device is asleep or your app is in the background.
- [struct AccessoryGPUWorker](./accessorygpuworker.md)
  A feature for GPU work that carries data between your data provider and transport extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessoryworker)*