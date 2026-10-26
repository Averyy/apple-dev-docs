# withUnsafeBufferPointer(_:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS
- watchOS 6.0+

## Declaration

```swift
func withUnsafeBufferPointer<R>(_ body: (UnsafeBufferPointer<Self.Element>) throws -> R) rethrows -> R
```

Available when `Self` conforms to `Collection`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/acceleratebuffer/withunsafebufferpointer(_:)-3oi0a)*