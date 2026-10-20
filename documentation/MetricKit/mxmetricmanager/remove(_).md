# remove(_:)

**Framework**: MetricKit  
**Kind**: method  
**Role**: Instance Method

Unsubscribes from daily reports of app metrics.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`MetricManager`](../metricmanager.md) instead.

## Declaration

```swift
func remove(_ subscriber: any MXMetricManagerSubscriber)
```

```objc
- (void) removeSubscriber:(id<MXMetricManagerSubscriber>) subscriber;
```

#### Discussion

> ⚠️ **Warning**:  If you call this function from a method that deallocates the object, your app might crash.

## Parameters

- `subscriber`: The object that receives daily metrics reports. Passing an object that is not currently subscribed does nothing.

## See Also

### Subscribing to reports
- [func add(any MXMetricManagerSubscriber)](./add%28_%29.md)
  Registers to receive a daily report of app metrics from the metrics manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetricmanager/remove(_:))*