# withUnsafeMutableBytes(_:)

**Framework**: Core Media  
**Kind**: method

Calls the given closure with a mutable pointer to the underlying bytes of the region’s contiguous storage.

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
func withUnsafeMutableBytes<ResultType>(_ body: (UnsafeMutableRawBufferPointer) throws -> ResultType) rethrows -> ResultType
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmutabledatablockbuffer/blockregion/withunsafemutablebytes(_:))*