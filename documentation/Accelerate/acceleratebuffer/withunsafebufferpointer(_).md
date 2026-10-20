# withUnsafeBufferPointer(_:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Calls a closure with a pointer to the object’s contiguous storage.

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

## Parameters

- `body`: A closure that receives an [`UnsafeBufferPointer`](../../Swift/unsafebufferpointer.md) to the sequence’s contiguous storage.

## Default Implementations

### AccelerateBuffer Implementations
- [func withUnsafeBufferPointer<R>((UnsafeBufferPointer<Self.Element>) throws -> R) rethrows -> R](./withunsafebufferpointer%28_%29-3oi0a.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/acceleratebuffer/withunsafebufferpointer(_:))*