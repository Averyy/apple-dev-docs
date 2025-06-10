# withUnsafeBytes(_:)

**Framework**: RealityKit  
**Kind**: method

Read the buffer synchronously on the CPU. The buffer provided is only valid for the lifetime of the callback.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func withUnsafeBytes(_ callback: (UnsafeRawBufferPointer) -> Void)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelbuffer/withunsafebytes(_:))*