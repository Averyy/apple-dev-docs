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
func withUnsafeMutablePointers<E, R>(_ body: (UnsafeMutablePointer<Header>, UnsafeMutablePointer<Element>) throws(E) -> R) throws(E) -> R where E : Error, R : ~Copyable
```

#### Discussion

> **Note**: These pointers are valid only for the duration of the call to `body`.

## See Also

- [func withUnsafeMutablePointerToElements<E, R>((UnsafeMutablePointer<Element>) throws(E) -> R) throws(E) -> R](managedbufferpointer/withunsafemutablepointertoelements(_:).md)
  Call `body` with an `UnsafeMutablePointer` to the `Element` storage.
- [func withUnsafeMutablePointerToHeader<E, R>((UnsafeMutablePointer<Header>) throws(E) -> R) throws(E) -> R](managedbufferpointer/withunsafemutablepointertoheader(_:).md)
  Call `body` with an `UnsafeMutablePointer` to the stored `Header`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/managedbufferpointer/withunsafemutablepointers(_:))*