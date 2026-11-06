# init(_:)

**Framework**: Accessory Transport Extension  
**Kind**: init  
**Role**: Initializer

Initializes a GPU worker feature with a handler factory.

**Availability**:
- iOS 27.3+ (Beta)

## Declaration

```swift
init(_ handlerFactory: @escaping @Sendable () -> any AccessoryFeatureSessionHandler<AccessoryGPUWorker.Session>)
```

## Discussion

Create the instance inside your data provider extension’s `extensionPoint`. The system calls the closure to create a new handler for each session. For more information, see [Sending data to an accessory in the background](../sending-data-to-an-accessory-in-the-background.md).

## Parameters

- `handlerFactory`: A closure that creates the handler for each session of the feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorygpuworker/init(_:))*