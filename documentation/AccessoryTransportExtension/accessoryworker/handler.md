# AccessoryWorker.Handler

**Framework**: Accessory Transport Extension  
**Kind**: typealias  
**Role**: Type Alias

A handler type for the session’s data provider.

**Availability**:
- iOS 27.3+ (Beta)

## Declaration

```swift
typealias Handler = AccessoryFeatureSessionHandler<AccessoryWorker.Session>
```

## Discussion

Conform your data provider extension’s handler to this type to receive events from an [`AccessoryWorker.Session`](./session.md). Because each feature uses its own `Handler` type alias, the compiler rejects a handler for this feature if you pass it to [`AccessoryGPUWorker`](../accessorygpuworker.md) or another feature. Return an instance of your handler from the factory closure that you pass to [`init(_:)`](./init%28_%29.md).

## See Also

### Handling data-provider sessions
- [AccessoryWorker.Session](./session.md)
  A class that represents the data provider within a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessoryworker/handler)*