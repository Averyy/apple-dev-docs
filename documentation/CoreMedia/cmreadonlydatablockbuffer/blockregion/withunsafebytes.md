# withUnsafeBytes(_:)

**Framework**: Core Media  
**Kind**: method

Calls the given closure with a pointer to the underlying bytes of the region’s contiguous storage.

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
func withUnsafeBytes<ResultType>(_ body: (UnsafeRawBufferPointer) throws -> ResultType) rethrows -> ResultType
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmreadonlydatablockbuffer/blockregion/withunsafebytes(_:))*