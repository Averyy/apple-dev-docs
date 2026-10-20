# CrashDiagnostic.TerminationReason

**Framework**: MetricKit  
**Kind**: struct  
**Role**: Structure

A value that describes the reason the app terminated.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct TerminationReason
```

#### Discussion

`TerminationReason` is [`RawRepresentable`](../../Swift/rawrepresentable.md) and [`CustomStringConvertible`](../../Swift/customstringconvertible.md). Use `rawValue` to access the underlying string value, or rely on the [`CustomStringConvertible`](../../Swift/customstringconvertible.md) conformance to print the termination reason or interpolate it into a string:

```swift
if let reason = diagnostic.terminationReason {
    print("Termination reason: \(reason)")
}
```

## Relationships

### Conforms To
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/crashdiagnostic/terminationreason-swift.struct)*