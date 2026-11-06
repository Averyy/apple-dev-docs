# AccessoryGPUWorker

**Framework**: Accessory Transport Extension  
**Kind**: struct  
**Role**: Structure

A feature for GPU work that carries data between your data provider and transport extensions.

**Availability**:
- iOS 27.3+ (Beta)

## Declaration

```swift
struct AccessoryGPUWorker
```

## Mentions

- [Sending data to an accessory in the background](./sending-data-to-an-accessory-in-the-background.md)

## Overview

An *accessory GPU worker* exchanges information in the background like [`AccessoryWorker`](./accessoryworker.md) does, but runs under a more permissive sandbox profile that permits GPU access. Create an instance of this structure in the `extensionPoint` of your [`AccessoryDataProvider`](./accessorydataprovider.md) extension, and open sessions from your transport extension with [`makeFeatureSession(_:)`](./accessorytransportsession/makefeaturesession%28_%29.md) in response to events from your accessory. Your app defines the data format, and the Accessory Transport Extension framework treats the data as opaque, with no additional encryption. Enroll the feature for each accessory with `requestAuthorization(for:)`. For more information, see [Sending data to an accessory in the background](./sending-data-to-an-accessory-in-the-background.md).

## Perform GPU work in the background

To perform work that requires the GPU in the background, you can use [Metal](../Metal/Metal.md), [Metal Performance Shaders](../MetalPerformanceShaders/MetalPerformanceShaders.md), [Core ML](../CoreML/CoreML.md) inference on the GPU or Neural Engine, and direct GPU memory access through Metal buffers ([`MTLBuffer`](../Metal/mtlbuffer.md)).

## Run a worker with scheduling and thermal limits

Use the GPU worker only when your accessory genuinely needs it. The system launches your GPU worker extension and keeps it running for as long as your accessory requires background GPU work for the accessory’s functionality. Because background work takes a lower priority than what’s running in the foreground, the system runs it at a background quality-of-service (QoS) level rather than real-time priority.

Build your extension to tolerate system pauses or session stops under thermal pressure so you can react to the unpredictable nature of background work.

## Topics

### Handling data-provider sessions
- [AccessoryGPUWorker.Handler](./accessorygpuworker/handler.md)
  A handler type for the session’s data provider.
- [AccessoryGPUWorker.Session](./accessorygpuworker/session.md)
  A class that represents the data provider within a session.
### Handling transport-extension sessions
- [AccessoryGPUWorker.FeatureSession](./accessorygpuworker/featuresession.md)
  A class that represents the session’s transport extension.
### Checking authorization
- [enum AccessoryFeatureAuthorizationStatus](./accessoryfeatureauthorizationstatus.md)
  A status that describes whether the system authorizes a feature for an accessory.
### Creating the feature
- [init(() -> any AccessoryFeatureSessionHandler<AccessoryGPUWorker.Session>)](./accessorygpuworker/init%28_%29.md)
  Initializes a GPU worker feature with a handler factory.

## Relationships

### Conforms To
- [AccessoryFeature](./accessoryfeature.md)
- [AccessoryFeatureAuthorizing](./accessoryfeatureauthorizing.md)
- [AppExtensionPoint.Capability](../ExtensionFoundation/appextensionpoint/capability.md)
- [Copyable](../Swift/copyable.md)
- [Escapable](../Swift/escapable.md)
- [Identifiable](../Swift/identifiable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Background work
- [Sending data to an accessory in the background](./sending-data-to-an-accessory-in-the-background.md)
  Move data between your accessory and your app when a person’s device is asleep or your app is in the background.
- [struct AccessoryWorker](./accessoryworker.md)
  A feature that carries data between your data provider and transport extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorygpuworker)*