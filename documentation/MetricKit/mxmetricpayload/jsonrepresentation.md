# jsonRepresentation()

**Framework**: MetricKit  
**Kind**: method

Returns the contents of the payload in JSON format.

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

A [`Data`](https://developer.apple.com/documentation/Foundation/Data) (Swift) or [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) (Objective-C) object containing the JSON representation of the metrics in the payload.

## See Also

- [func dictionaryRepresentation() -> [AnyHashable : Any]](mxmetricpayload/dictionaryrepresentation.md)
  Returns the results of the payload as a dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetricpayload/jsonrepresentation())*