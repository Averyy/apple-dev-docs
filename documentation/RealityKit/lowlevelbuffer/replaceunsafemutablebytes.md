# replaceUnsafeMutableBytes(_:)

**Framework**: RealityKit  
**Kind**: method

Replace the buffer’s contents synchronously on the CPU.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final func replaceUnsafeMutableBytes(_ callback: (UnsafeMutableRawBufferPointer) -> Void)
```

#### Discussion

The buffer’s contents are unspecified, and it is the caller’s responsibility to populate the buffer with valid data. The buffer provided is only valid for the lifetime of the callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelbuffer/replaceunsafemutablebytes(_:))*