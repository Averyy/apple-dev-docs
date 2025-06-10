# dictionaryRepresentation()

**Framework**: MetricKit  
**Kind**: method

Returns the contents of a metric as a dictionary.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func dictionaryRepresentation() -> [AnyHashable : Any]
```

#### Return Value

A [`Dictionary`](https://developer.apple.com/documentation/Swift/Dictionary) (Swift) or [`NSDictionary`](https://developer.apple.com/documentation/Foundation/NSDictionary) (Objective-C) object containing a key-value representation of the metrics in the payload.

## See Also

- [func jsonRepresentation() -> Data](mxmetric/jsonrepresentation.md)
  Returns the contents of the metric in JSON format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetric/dictionaryrepresentation())*