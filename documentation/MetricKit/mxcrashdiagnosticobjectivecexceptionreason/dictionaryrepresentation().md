# dictionaryRepresentation()

**Framework**: MetricKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 17.0+ - Deprecated in 27.2
- iPadOS 17.0+ - Deprecated in 27.2
- Mac Catalyst 17.0+ - Deprecated in 27.0
- macOS 14.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`CrashDiagnostic.ObjectiveCExceptionReason`](../crashdiagnostic/objectivecexceptionreason.md) instead.

## Declaration

```swift
func dictionaryRepresentation() -> [AnyHashable : Any]
```

```objc
- (NSDictionary *) dictionaryRepresentation;
```

## See Also

### Generating a report
- [func jsonRepresentation() -> Data](./jsonrepresentation%28%29.md)
  Returns the contents of the exception reason in JSON format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxcrashdiagnosticobjectivecexceptionreason/dictionaryrepresentation())*