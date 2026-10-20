# hashFunction

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The hash function.

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
var hashFunction: ((UnsafeRawPointer, ((UnsafeRawPointer) -> Int)?) -> Int)? { get set }
```

```objc
@property (nullable) unsigned long (*)(const void *, unsigned long (*)(const void *)) hashFunction;
```

## See Also

### Personality Functions
- [var isEqualFunction: ((UnsafeRawPointer, UnsafeRawPointer, ((UnsafeRawPointer) -> Int)?) -> ObjCBool)?](./isequalfunction.md)
  The function used to compare pointers.
- [var sizeFunction: ((UnsafeRawPointer) -> Int)?](./sizefunction.md)
  The function used to determine the size of pointers.
- [var descriptionFunction: ((UnsafeRawPointer) -> String?)?](./descriptionfunction.md)
  The function used to describe elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspointerfunctions/hashfunction)*