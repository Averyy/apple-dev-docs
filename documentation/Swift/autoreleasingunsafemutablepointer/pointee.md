# pointee

**Framework**: Swift  
**Kind**: property

Retrieve or set the `Pointee` instance referenced by `self`.

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
var pointee: Pointee { get nonmutating set }
```

#### Discussion

`AutoreleasingUnsafeMutablePointer` is assumed to reference a value with `__autoreleasing` ownership semantics, like `NSFoo **` declarations in ARC. Setting the pointee autoreleases the new value before trivially storing it in the referenced memory.

> **Note**: The pointee has been initialized with an instance of type `Pointee`.

The pointee has been initialized with an instance of type `Pointee`.

## See Also

- [subscript(Int) -> Pointee](autoreleasingunsafemutablepointer/subscript(_:).md)
  Access the `i`th element of the raw array pointed to by `self`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/autoreleasingunsafemutablepointer/pointee)*