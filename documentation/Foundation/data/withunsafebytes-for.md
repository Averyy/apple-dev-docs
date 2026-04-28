# withUnsafeBytes(for:_:)

**Framework**: Foundation  
**Kind**: method

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+
- Swift 6.2+
- Xcode 26.0+

## Declaration

```swift
func withUnsafeBytes<R>(for attachment: borrowing Attachment<Data>, _ body: (UnsafeRawBufferPointer) throws -> R) throws -> R
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/withunsafebytes(for:_:))*