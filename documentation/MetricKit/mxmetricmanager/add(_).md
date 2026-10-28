# add(_:)

**Framework**: MetricKit  
**Kind**: method  
**Role**: Instance Method

Registers to receive a daily report of app metrics from the metrics manager.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`MetricManager`](../metricmanager.md) instead.

## Declaration

```swift
func add(_ subscriber: any MXMetricManagerSubscriber)
```

```objc
- (void) addSubscriber:(id<MXMetricManagerSubscriber>) subscriber;
```

## Discussion

> ⚠️ **Warning**:  If you call this function from a method that deallocates the object, your app might crash.

## Parameters

- `subscriber`: The object that receives the daily metrics reports. The object must conform to [`MXMetricManagerSubscriber`](../mxmetricmanagersubscriber.md).

## See Also

### Subscribing to reports
- [func remove(any MXMetricManagerSubscriber)](./remove%28_%29.md)
  Unsubscribes from daily reports of app metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetricmanager/add(_:))*