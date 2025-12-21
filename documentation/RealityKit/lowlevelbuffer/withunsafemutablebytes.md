# withUnsafeMutableBytes(_:)

**Framework**: RealityKit  
**Kind**: method

Update the buffer’s contents synchronously on the CPU. The buffer provided is only valid for the lifetime of the callback.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final func withUnsafeMutableBytes(_ callback: (UnsafeMutableRawBufferPointer) -> Void)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelbuffer/withunsafemutablebytes(_:))*