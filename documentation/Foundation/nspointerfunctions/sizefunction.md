# sizeFunction

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The function used to determine the size of pointers.

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
var sizeFunction: ((UnsafeRawPointer) -> Int)? { get set }
```

```objc
@property (nullable) unsigned long (*)(const void *) sizeFunction;
```

#### Discussion

This function is used for copy-in operations (unless the collection has an object personality).

## See Also

### Personality Functions
- [var hashFunction: ((UnsafeRawPointer, ((UnsafeRawPointer) -> Int)?) -> Int)?](./hashfunction.md)
  The hash function.
- [var isEqualFunction: ((UnsafeRawPointer, UnsafeRawPointer, ((UnsafeRawPointer) -> Int)?) -> ObjCBool)?](./isequalfunction.md)
  The function used to compare pointers.
- [var descriptionFunction: ((UnsafeRawPointer) -> String?)?](./descriptionfunction.md)
  The function used to describe elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspointerfunctions/sizefunction)*