# jsonRepresentation()

**Framework**: MetricKit  
**Kind**: method  
**Role**: Instance Method

Returns the contents of the exception reason in JSON format.

**Availability**:
- iOS 17.0+ - Deprecated in 27.2
- iPadOS 17.0+ - Deprecated in 27.2
- Mac Catalyst 17.0+ - Deprecated in 27.0
- macOS 14.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`CrashDiagnostic.ObjectiveCExceptionReason`](../crashdiagnostic/objectivecexceptionreason.md) instead.

## Declaration

```swift
func jsonRepresentation() -> Data
```

```objc
- (NSData *) JSONRepresentation;
```

## Return Value

An [`NSData`](../../Foundation/nsdata.md) object containing the JSON representation of the metrics in the payload.

## See Also

### Generating a report
- [func dictionaryRepresentation() -> [AnyHashable : Any]](./dictionaryrepresentation%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxcrashdiagnosticobjectivecexceptionreason/jsonrepresentation())*