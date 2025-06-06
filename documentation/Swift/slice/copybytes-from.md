# copyBytes(from:)

**Framework**: Swift  
**Kind**: method

Copies from a collection of `UInt8` into this buffer slice’s memory.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func copyBytes<C>(from source: C) where C : Collection, C.Element == UInt8
```

#### Discussion

If the first `source.count` bytes of memory referenced by this buffer slice are bound to a type `T`, then `T` must be a trivial type, the underlying pointer must be properly aligned for accessing `T`, and `source.count` must be a multiple of `MemoryLayout<T>.stride`.

After calling `copyBytes(from:)`, the first `source.count` bytes of memory referenced by this buffer slice are initialized to raw bytes. If the memory is bound to type `T`, then it contains values of type `T`.

## Parameters

- `source`: A collection of   elements.   must   be less than or equal to this buffer slice’s  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/slice/copybytes(from:))*