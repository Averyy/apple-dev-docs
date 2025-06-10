# remove(_:)

**Framework**: MetricKit  
**Kind**: method

Unsubscribes from daily reports of app metrics.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func remove(_ subscriber: any MXMetricManagerSubscriber)
```

#### Discussion

> ⚠️ **Warning**:  If you call this function from a method that deallocates the object, your app might crash.

## Parameters

- `subscriber`: The object that receives daily metrics reports. Passing an object that is not currently subscribed does nothing.

## See Also

- [func add(any MXMetricManagerSubscriber)](mxmetricmanager/add(_:).md)
  Registers to receive a daily report of app metrics from the metrics manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetricmanager/remove(_:))*