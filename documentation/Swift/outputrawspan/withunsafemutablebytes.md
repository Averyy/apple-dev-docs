# withUnsafeMutableBytes(_:)

**Framework**: Swift  
**Kind**: method

Call the given closure with the unsafe buffer pointer addressed by this OutputRawSpan and a mutable reference to its count of initialized bytes.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 12.2+
- macOS 10.14.4+
- tvOS 12.2+
- visionOS 1.0+
- watchOS 5.2+

## Declaration

```swift
mutating func withUnsafeMutableBytes<E, R>(_ body: (UnsafeMutableRawBufferPointer, inout Int) throws(E) -> R) throws(E) -> R where E : Error, R : ~Copyable
```

#### Discussion

This method provides a way to process or populate an `OutputRawSpan` using unsafe operations, such as dispatching to code written in legacy (memory-unsafe) languages.

The supplied closure may process the buffer in any way it wants; however, when it finishes (whether by returning or throwing), it must leave the buffer in a state that satisfies the invariants of the output span:

1. The inout integer passed in as the second argument must be the exact number of initialized bytes in the buffer passed in as the first argument.
2. These initialized elements must be located in a single contiguous region starting at the beginning of the buffer. The rest of the buffer must hold uninitialized memory.

This function cannot verify these two invariants, and therefore this is an unsafe operation. Violating the invariants of `OutputRawSpan` may result in undefined behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/outputrawspan/withunsafemutablebytes(_:))*