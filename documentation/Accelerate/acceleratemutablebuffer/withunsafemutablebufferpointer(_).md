# withUnsafeMutableBufferPointer(_:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Calls the given closure with a pointer to the object’s mutable contiguous storage.

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

## Parameters

- `body`: A closure that receives an [`UnsafeMutableBufferPointer`](../../Swift/unsafemutablebufferpointer.md) to the sequence’s contiguous storage.

## Default Implementations

### AccelerateMutableBuffer Implementations
- [func withUnsafeMutableBufferPointer<R>((inout UnsafeMutableBufferPointer<Self.Element>) throws -> R) rethrows -> R](./withunsafemutablebufferpointer%28_%29-5wvde.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/acceleratemutablebuffer/withunsafemutablebufferpointer(_:))*