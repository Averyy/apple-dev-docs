# withUnsafeMutableBufferPointer(_:)

**Framework**: Accelerate  
**Kind**: method  
**Required**: Yes

Calls the given closure with a pointer to the object’s mutable contiguous storage.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
mutating func withUnsafeMutableBufferPointer<R>(_ body: (inout UnsafeMutableBufferPointer<Self.Element>) throws -> R) rethrows -> R
```

## Parameters

- `body`: A closure that receives an   to the sequence’s contiguous storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/acceleratemutablebuffer/withunsafemutablebufferpointer(_:))*