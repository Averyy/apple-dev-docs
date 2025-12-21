# withUnsafeBlockRegions(_:)

**Framework**: Core Media  
**Kind**: method

Access the potentially non-contiguous memory region referenced by this block buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func withUnsafeBlockRegions<R>(_ body: ([CMReadOnlyDataBlockBuffer.BlockRegion]) throws -> sending R) rethrows -> sending R
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmutabledatablockbuffer/withunsafeblockregions(_:))*