# jsonRepresentation()

**Framework**: MetricKit  
**Kind**: method  
**Role**: Instance Method

Returns the contents of the diagnostic in JSON format.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`DiagnosticResult`](../diagnosticresult.md) instead.

## Declaration

```swift
func jsonRepresentation() -> Data
```

```objc
- (NSData *) JSONRepresentation;
```

#### Return Value

A [`Data`](../../Foundation/data.md) (Swift) or [`NSData`](../../Foundation/nsdata.md) (Objective-C) object containing the JSON representation of the contents of the diagnostic.

## See Also

### Generating a report
- [func dictionaryRepresentation() -> [AnyHashable : Any]](./dictionaryrepresentation%28%29.md)
  Returns the contents of a diagnostic as a dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxdiagnostic/jsonrepresentation())*