# descriptionFunction

**Framework**: Foundation  
**Kind**: property

The function used to describe elements.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var descriptionFunction: ((UnsafeRawPointer) -> String?)? { get set }
```

#### Discussion

This function is used by description methods for hash and map tables.

## See Also

- [var hashFunction: ((UnsafeRawPointer, ((UnsafeRawPointer) -> Int)?) -> Int)?](nspointerfunctions/hashfunction.md)
  The hash function.
- [var isEqualFunction: ((UnsafeRawPointer, UnsafeRawPointer, ((UnsafeRawPointer) -> Int)?) -> ObjCBool)?](nspointerfunctions/isequalfunction.md)
  The function used to compare pointers.
- [var sizeFunction: ((UnsafeRawPointer) -> Int)?](nspointerfunctions/sizefunction.md)
  The function used to determine the size of pointers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspointerfunctions/descriptionfunction)*