# dictionaryRepresentation()

**Framework**: MetricKit  
**Kind**: method

Returns the contents of the metadata as a dictionary.

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

A [`Dictionary`](https://developer.apple.com/documentation/Swift/Dictionary) (Swift) or [`NSDictionary`](https://developer.apple.com/documentation/Foundation/NSDictionary) (Objective-C) object containing a key-value representation of the contents of the metadata.

## See Also

- [func jsonRepresentation() -> Data](mxmetadata/jsonrepresentation.md)
  Returns the contents of the metadata in JSON format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetadata/dictionaryrepresentation())*