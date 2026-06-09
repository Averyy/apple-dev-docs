# binaryUUID

**Framework**: MetricKit  
**Kind**: property

Binary UUID (references CallStackTree.binaryInfo)

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
let binaryUUID: UUID?
```

## Mentions

- [Analyzing app performance with MetricKit](analyzing-app-performance-with-metrickit.md)

#### Discussion

This may be nil if symbolication information is unavailable or the binary is unidentified.

## See Also

- [let address: UInt64?](callstackframe/address.md)
  Absolute address
- [let offsetIntoBinaryTextSegment: UInt64?](callstackframe/offsetintobinarytextsegment.md)
  Offset into binary text segment
- [let sampleCount: Int?](callstackframe/samplecount.md)
  Sample count (for sampled stack traces)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/callstackframe/binaryuuid)*