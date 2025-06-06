# jsonRepresentation()

**Framework**: MetricKit  
**Kind**: method

Returns the contents of the metric in JSON format.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func jsonRepresentation() -> Data
```

#### Return Value

A [`Data`](https://developer.apple.com/documentation/Foundation/Data) (Swift) or [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) (Objective-C) object containing the JSON representation of the contents of the metric.

## See Also

- [func dictionaryRepresentation() -> [AnyHashable : Any]](mxmetric/dictionaryrepresentation.md)
  Returns the contents of a metric as a Dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetric/jsonrepresentation())*