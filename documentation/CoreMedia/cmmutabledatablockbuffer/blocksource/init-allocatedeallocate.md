# init(allocate:deallocate:)

**Framework**: Core Media  
**Kind**: init

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
init(allocate: @escaping (Int) -> UnsafeMutableRawBufferPointer, deallocate: @escaping (UnsafeMutableRawBufferPointer) -> Void)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmutabledatablockbuffer/blocksource/init(allocate:deallocate:))*