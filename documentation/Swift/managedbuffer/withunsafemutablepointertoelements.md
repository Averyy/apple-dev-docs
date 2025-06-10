# withUnsafeMutablePointerToElements(_:)

**Framework**: Swift  
**Kind**: method

Call `body` with an `UnsafeMutablePointer` to the `Element` storage.

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
final func withUnsafeMutablePointerToElements<E, R>(_ body: (UnsafeMutablePointer<Element>) throws(E) -> R) throws(E) -> R where E : Error, R : ~Copyable
```

#### Discussion

> **Note**: This pointer is valid only for the duration of the call to `body`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/managedbuffer/withunsafemutablepointertoelements(_:))*