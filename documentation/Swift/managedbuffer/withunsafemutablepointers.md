# withUnsafeMutablePointers(_:)

**Framework**: Swift  
**Kind**: method

Call `body` with `UnsafeMutablePointer`s to the stored `Header` and raw `Element` storage.

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
final func withUnsafeMutablePointers<E, R>(_ body: (UnsafeMutablePointer<Header>, UnsafeMutablePointer<Element>) throws(E) -> R) throws(E) -> R where E : Error, R : ~Copyable
```

#### Discussion

> **Note**: These pointers are valid only for the duration of the call to `body`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/managedbuffer/withunsafemutablepointers(_:))*