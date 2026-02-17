# withUnsafeBytes(for:_:)

**Framework**: Swift  
**Kind**: method

**Availability**:
- Swift 6.2+
- Xcode 26.0+

## Declaration

```swift
func withUnsafeBytes<R>(for attachment: borrowing Attachment<String>, _ body: (UnsafeRawBufferPointer) throws -> R) throws -> R
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/withunsafebytes(for:_:))*