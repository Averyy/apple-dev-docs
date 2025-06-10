# withUnsafeMutableBlockRegions(_:)

**Framework**: Core Media  
**Kind**: method

Access the potentially non-contiguous memory region referenced by this block buffer.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
mutating func withUnsafeMutableBlockRegions<R>(_ body: ([CMMutableDataBlockBuffer.BlockRegion]) throws -> sending R) rethrows -> sending R
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmutabledatablockbuffer/withunsafemutableblockregions(_:))*