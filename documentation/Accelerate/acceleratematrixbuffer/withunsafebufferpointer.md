# withUnsafeBufferPointer(_:)

**Framework**: Accelerate  
**Kind**: method  
**Required**: Yes

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS ?+
- watchOS 11.0+

## Declaration

```swift
func withUnsafeBufferPointer<R>(_ body: (UnsafeBufferPointer<Self.Element>) throws -> R) rethrows -> R
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/acceleratematrixbuffer/withunsafebufferpointer(_:))*