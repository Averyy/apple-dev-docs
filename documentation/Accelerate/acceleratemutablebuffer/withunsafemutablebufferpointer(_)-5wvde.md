# withUnsafeMutableBufferPointer(_:)

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
mutating func withUnsafeMutableBufferPointer<R>(_ body: (inout UnsafeMutableBufferPointer<Self.Element>) throws -> R) rethrows -> R
```

Available when `Self` conforms to `MutableCollection`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/acceleratemutablebuffer/withunsafemutablebufferpointer(_:)-5wvde)*