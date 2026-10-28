# withUnsafeMutablePointers(_:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

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

## Discussion

> **Note**: These pointers are valid only for the duration of the call to `body`. The caller is responsible for ensuring that the buffer is not being accessed elsewhere while performing this call.

## See Also

### Accessing Buffer Contents
- [func withUnsafeMutablePointerToElements<E, R>((UnsafeMutablePointer<Element>) throws(E) -> R) throws(E) -> R](./withunsafemutablepointertoelements%28_%29.md)
  Call `body` with an `UnsafeMutablePointer` to the `Element` storage.
- [func withUnsafeMutablePointerToHeader<E, R>((UnsafeMutablePointer<Header>) throws(E) -> R) throws(E) -> R](./withunsafemutablepointertoheader%28_%29.md)
  Call `body` with an `UnsafeMutablePointer` to the stored `Header`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/managedbufferpointer/withunsafemutablepointers(_:))*