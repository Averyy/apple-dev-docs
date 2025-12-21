# withUnsafeBytes(for:_:)

**Framework**: Foundation  
**Kind**: method

**Availability**:
- Swift 6.2+
- Xcode 26.0+

## Declaration

```swift
func withUnsafeBytes<R>(for attachment: borrowing Attachment<Data>, _ body: (UnsafeRawBufferPointer) throws -> R) throws -> R
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/withunsafebytes(for:_:))*