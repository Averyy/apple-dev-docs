# address

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

Absolute address

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
let address: UInt64?
```

## Discussion

This may be nil if the address information could not be collected.

## See Also

### Frame details
- [let binaryUUID: UUID?](./binaryuuid.md)
  Binary UUID (references CallStackTree.binaryInfo)
- [let offsetIntoBinaryTextSegment: UInt64?](./offsetintobinarytextsegment.md)
  Offset into binary text segment
- [let sampleCount: Int?](./samplecount.md)
  Sample count (for sampled stack traces)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/callstackframe/address)*