# descriptionFunction

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nullable) NSString *(*)(const void *) descriptionFunction;
```

## Discussion

This function is used by description methods for hash and map tables.

## See Also

### Personality Functions
- [var hashFunction: ((UnsafeRawPointer, ((UnsafeRawPointer) -> Int)?) -> Int)?](./hashfunction.md)
  The hash function.
- [var isEqualFunction: ((UnsafeRawPointer, UnsafeRawPointer, ((UnsafeRawPointer) -> Int)?) -> ObjCBool)?](./isequalfunction.md)
  The function used to compare pointers.
- [var sizeFunction: ((UnsafeRawPointer) -> Int)?](./sizefunction.md)
  The function used to determine the size of pointers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspointerfunctions/descriptionfunction)*