# copyBytes(to:from:)

**Framework**: Core Media  
**Kind**: method

Copy the bytes from the given range to the destination buffer.

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
func copyBytes<R>(to destination: UnsafeMutableRawBufferPointer, from range: R) where R : RangeExpression, R.Bound == Int
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmutabledatablockbuffer/copybytes(to:from:))*