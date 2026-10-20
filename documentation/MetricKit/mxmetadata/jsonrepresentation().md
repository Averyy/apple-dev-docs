# jsonRepresentation()

**Framework**: MetricKit  
**Kind**: method  
**Role**: Instance Method

Returns the contents of the metadata in JSON format.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`MetricReport.Environment`](../metricreport/environment-swift.struct.md) or [`DiagnosticReport.Environment`](../diagnosticreport/environment-swift.struct.md) instead.

## Declaration

```swift
func jsonRepresentation() -> Data
```

```objc
- (NSData *) JSONRepresentation;
```

#### Return Value

A [`Data`](../../Foundation/data.md) (Swift) or [`NSData`](../../Foundation/nsdata.md) (Objective-C)  object containing the JSON representation of the contents of the metadata.

## See Also

### Generating a report
- [func dictionaryRepresentation() -> [AnyHashable : Any]](./dictionaryrepresentation%28%29.md)
  Returns the contents of the metadata as a dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetadata/jsonrepresentation())*