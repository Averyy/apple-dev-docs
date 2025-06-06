# isEqualFunction

**Framework**: Foundation  
**Kind**: property

The function used to compare pointers.

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
var isEqualFunction: ((UnsafeRawPointer, UnsafeRawPointer, ((UnsafeRawPointer) -> Int)?) -> ObjCBool)? { get set }
```

## See Also

- [var hashFunction: ((UnsafeRawPointer, ((UnsafeRawPointer) -> Int)?) -> Int)?](nspointerfunctions/hashfunction.md)
  The hash function.
- [var sizeFunction: ((UnsafeRawPointer) -> Int)?](nspointerfunctions/sizefunction.md)
  The function used to determine the size of pointers.
- [var descriptionFunction: ((UnsafeRawPointer) -> String?)?](nspointerfunctions/descriptionfunction.md)
  The function used to describe elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspointerfunctions/isequalfunction)*