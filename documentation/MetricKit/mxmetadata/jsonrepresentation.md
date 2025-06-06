# jsonRepresentation()

**Framework**: MetricKit  
**Kind**: method

Returns the contents of the metadata in JSON format.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func jsonRepresentation() -> Data
```

#### Return Value

A [`Data`](https://developer.apple.com/documentation/Foundation/Data) (Swift) or [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) (Objective-C)  object containing the JSON representation of the contents of the metadata.

## See Also

- [func dictionaryRepresentation() -> [AnyHashable : Any]](mxmetadata/dictionaryrepresentation.md)
  Returns the contents of the metadata as a dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetadata/jsonrepresentation())*