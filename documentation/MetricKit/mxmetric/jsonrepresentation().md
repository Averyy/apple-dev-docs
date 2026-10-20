# jsonRepresentation()

**Framework**: MetricKit  
**Kind**: method  
**Role**: Instance Method

Returns the contents of the metric in JSON format.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`MetricResult`](../metricresult.md) instead.

## Declaration

```swift
func jsonRepresentation() -> Data
```

```objc
- (NSData *) JSONRepresentation;
```

#### Return Value

A [`Data`](../../Foundation/data.md) (Swift) or [`NSData`](../../Foundation/nsdata.md) (Objective-C) object containing the JSON representation of the contents of the metric.

## See Also

### Generate a report
- [func dictionaryRepresentation() -> [AnyHashable : Any]](./dictionaryrepresentation%28%29.md)
  Returns the contents of a metric as a dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetric/jsonrepresentation())*