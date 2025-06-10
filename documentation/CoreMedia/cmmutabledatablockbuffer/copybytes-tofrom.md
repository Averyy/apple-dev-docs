# copyBytes(to:from:)

**Framework**: Core Media  
**Kind**: method

Copy the bytes from the given range to the destination buffer.

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
func copyBytes<R>(to destination: UnsafeMutableRawBufferPointer, from range: R) where R : RangeExpression, R.Bound == Int
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmutabledatablockbuffer/copybytes(to:from:))*