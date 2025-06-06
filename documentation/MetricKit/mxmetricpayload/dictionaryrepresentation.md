# dictionaryRepresentation()

**Framework**: MetricKit  
**Kind**: method

Returns the results of the payload as a dictionary.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func dictionaryRepresentation() -> [AnyHashable : Any]
```

#### Return Value

A [`Dictionary`](https://developer.apple.com/documentation/Swift/Dictionary) (Swift) or [`NSDictionary`](https://developer.apple.com/documentation/Foundation/NSDictionary) (Objective-C) object containing a key-value representation of the metrics in the payload.

## See Also

- [func jsonRepresentation() -> Data](mxmetricpayload/jsonrepresentation.md)
  Returns the contents of the payload in JSON format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetricpayload/dictionaryrepresentation())*