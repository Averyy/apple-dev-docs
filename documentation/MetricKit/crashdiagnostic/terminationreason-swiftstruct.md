# CrashDiagnostic.TerminationReason

**Framework**: MetricKit  
**Kind**: struct

A value that describes the reason the app terminated.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct TerminationReason
```

#### Discussion

`TerminationReason` is [`RawRepresentable`](https://developer.apple.com/documentation/swift/rawrepresentable) and [`CustomStringConvertible`](https://developer.apple.com/documentation/swift/customstringconvertible). Use `rawValue` to access the underlying string value, or rely on the [`CustomStringConvertible`](https://developer.apple.com/documentation/swift/customstringconvertible) conformance to print the termination reason or interpolate it into a string:

```swift
if let reason = diagnostic.terminationReason {
    print("Termination reason: \(reason)")
}
```

## Relationships

### Conforms To
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/crashdiagnostic/terminationreason-swift.struct)*