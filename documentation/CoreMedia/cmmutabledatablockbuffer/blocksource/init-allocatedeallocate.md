# init(allocate:deallocate:)

**Framework**: Core Media  
**Kind**: init

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
init(allocate: @escaping (Int) -> UnsafeMutableRawBufferPointer, deallocate: @escaping (UnsafeMutableRawBufferPointer) -> Void)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmutabledatablockbuffer/blocksource/init(allocate:deallocate:))*