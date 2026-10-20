# dictionaryRepresentation()

**Framework**: MetricKit  
**Kind**: method  
**Role**: Instance Method

Returns the contents of the metadata as a dictionary.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`MetricReport.Environment`](../metricreport/environment-swift.struct.md) or [`DiagnosticReport.Environment`](../diagnosticreport/environment-swift.struct.md) instead.

## Declaration

```swift
func dictionaryRepresentation() -> [AnyHashable : Any]
```

```objc
- (NSDictionary *) dictionaryRepresentation;
```

#### Return Value

A [`Dictionary`](../../Swift/dictionary.md) (Swift) or [`NSDictionary`](../../Foundation/nsdictionary.md) (Objective-C) object containing a key-value representation of the metrics in the payload.

## See Also

### Generating a report
- [func jsonRepresentation() -> Data](./jsonrepresentation%28%29.md)
  Returns the contents of the metadata in JSON format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetadata/dictionaryrepresentation())*