---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/flatmap(_:)-40jd1"
framework: "swift-configuration/Configuration"
---

# flatMap(_:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.flatMap(_:)`.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
@preconcurrency
func flatMap<SegmentOfResult>(_ transform: @escaping @Sendable (Self.Element) async -> SegmentOfResult) -> AsyncFlatMapSequence<Self, SegmentOfResult> where SegmentOfResult : AsyncSequence, Self.Failure == SegmentOfResult.Failure
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/flatmap(_:)-40jd1)*