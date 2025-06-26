# withUnsafeMutableBytes(_:)

**Framework**: RealityKit  
**Kind**: method

Update the buffer’s contents synchronously on the CPU. The buffer provided is only valid for the lifetime of the callback.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
final func withUnsafeMutableBytes(_ callback: (UnsafeMutableRawBufferPointer) -> Void)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelbuffer/withunsafemutablebytes(_:))*