# AccessoryGPUWorker.Handler

**Framework**: Accessory Transport Extension  
**Kind**: typealias  
**Role**: Type Alias

A handler type for the session’s data provider.

**Availability**:
- iOS 27.3+ (Beta)

## Declaration

```swift
typealias Handler = AccessoryFeatureSessionHandler<AccessoryGPUWorker.Session>
```

## Mentions

- [Sending data to an accessory in the background](../sending-data-to-an-accessory-in-the-background.md)

## Discussion

Conform your data provider extension’s handler to this type to receive events from an [`AccessoryGPUWorker.Session`](./session.md). Because each feature uses its own `Handler` type alias, the compiler rejects a handler for this feature if you pass it to [`AccessoryWorker`](../accessoryworker.md) or another feature. Return an instance of your handler from the factory closure that you pass to [`init(_:)`](./init%28_%29.md).

## See Also

### Handling data-provider sessions
- [AccessoryGPUWorker.Session](./session.md)
  A class that represents the data provider within a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorygpuworker/handler)*