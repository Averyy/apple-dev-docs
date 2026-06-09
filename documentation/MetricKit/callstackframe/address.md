# address

**Framework**: MetricKit  
**Kind**: property

Absolute address

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
let address: UInt64?
```

#### Discussion

This may be nil if the address information could not be collected.

## See Also

- [let binaryUUID: UUID?](callstackframe/binaryuuid.md)
  Binary UUID (references CallStackTree.binaryInfo)
- [let offsetIntoBinaryTextSegment: UInt64?](callstackframe/offsetintobinarytextsegment.md)
  Offset into binary text segment
- [let sampleCount: Int?](callstackframe/samplecount.md)
  Sample count (for sampled stack traces)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/callstackframe/address)*