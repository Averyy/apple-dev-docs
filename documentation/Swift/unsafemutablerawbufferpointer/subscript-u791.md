# subscript(_:)

**Framework**: Swift  
**Kind**: subscript

Accesses the byte at the given offset in the memory region as a `UInt8` value.

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
subscript(i: Int) -> UnsafeMutableRawBufferPointer.Element { get nonmutating set }
```

## Parameters

- `i`: The offset of the byte to access.   must be in the range   .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablerawbufferpointer/subscript(_:)-u791)*