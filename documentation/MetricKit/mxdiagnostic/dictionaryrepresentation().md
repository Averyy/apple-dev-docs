# dictionaryRepresentation()

**Framework**: MetricKit  
**Kind**: method  
**Role**: Instance Method

Returns the contents of a diagnostic as a dictionary.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`DiagnosticResult`](../diagnosticresult.md) instead.

## Declaration

```swift
func dictionaryRepresentation() -> [AnyHashable : Any]
```

```objc
- (NSDictionary *) dictionaryRepresentation;
```

## Return Value

A [`Dictionary`](../../Swift/dictionary.md) (Swift) or [`NSDictionary`](../../Foundation/nsdictionary.md) (Objective-C) object containing the JSON representation of the contents of the diagnostic.

## See Also

### Generating a report
- [func jsonRepresentation() -> Data](./jsonrepresentation%28%29.md)
  Returns the contents of the diagnostic in JSON format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxdiagnostic/dictionaryrepresentation())*