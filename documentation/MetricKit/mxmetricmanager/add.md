# add(_:)

**Framework**: MetricKit  
**Kind**: method

Registers to receive a daily report of app metrics from the metrics manager.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func add(_ subscriber: any MXMetricManagerSubscriber)
```

#### Discussion

> ⚠️ **Warning**:  If you call this function from a method that deallocates the object, your app might crash.

## Parameters

- `subscriber`: The object that receives the daily metrics reports. The object must conform to  .

## See Also

- [func remove(any MXMetricManagerSubscriber)](mxmetricmanager/remove(_:).md)
  Unsubscribes from daily reports of app metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetricmanager/add(_:))*