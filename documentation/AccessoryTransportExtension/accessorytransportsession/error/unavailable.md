# AccessoryTransportSession.Error.unavailable

**Framework**: Accessory Transport Extension  
**Kind**: case  
**Role**: Case

An error that indicates the feature isn’t available on the device.

**Availability**:
- iOS 27.3+ (Beta)

## Declaration

```swift
case unavailable
```

## Discussion

[`activate()`](../../accessoryfeatureruntimesession/activate%28%29.md) and `AccessoryWorker/requestAuthorization(for:)` (and the matching `AccessoryGPUWorker/requestAuthorization(for:)`) throw this error when the system determines that the feature isn’t currently eligible to run on the device. [`makeFeatureSession(_:)`](../makefeaturesession%28_%29.md) doesn’t throw it. If a device loses eligibility while a feature session is already running, the system reports the error through [`sessionInvalidated(error:)`](../../accessoryfeatureruntimesessionhandler/sessioninvalidated%28error%29.md) instead.

Region is the only eligibility check behind this error. The framework restricts [`AccessoryWorker`](../../accessoryworker.md) and [`AccessoryGPUWorker`](../../accessorygpuworker.md) to the EU-region devices described in [Accessory Transport Extension](../../AccessoryTransportExtension.md). The system doesn’t restrict eligibility by device class.

## See Also

### Identifying session errors
- [AccessoryTransportSession.Error.invalidated](./invalidated.md)
  An error that indicates the session is invalidated.
- [AccessoryTransportSession.Error.unsupported](./unsupported.md)
  An error that indicates a client-provided value or operation isn’t supported.
- [AccessoryTransportSession.Error.unknown](./unknown.md)
  An error that indicates a failure with an unknown cause.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsession/error/unavailable)*