# withUTF8(_:)

**Framework**: Swift  
**Kind**: method

Runs `body` over the content of this substring in contiguous memory. If this substring is not contiguous, this will first make it contiguous, which will also speed up subsequent access. If this mutates the substring, it will invalidate any pre-existing indices.

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
mutating func withUTF8<R>(_ body: (UnsafeBufferPointer<UInt8>) throws -> R) rethrows -> R
```

#### Discussion

Note that it is unsafe to escape the pointer provided to `body`. For example, strings of up to 15 UTF-8 code units in length may be represented in a small-string representation, and thus will be spilled into temporary stack space which is invalid after `withUTF8` finishes execution.

Complexity: O(n) if non-contiguous, O(1) if already contiguous


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/substring/withutf8(_:))*