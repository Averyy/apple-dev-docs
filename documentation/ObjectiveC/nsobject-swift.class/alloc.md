# alloc

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Type Method

Returns a new instance of the receiving class.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```objc
+ (instancetype) alloc;
```

## Return Value

A new instance of the receiver.

## Discussion

This is an instance variable of the new instance that is initialized to a data structure describing the class; memory for all other instance variables is set to `0`.

You must use an `init...` method to complete the initialization process. For example:

```objc
TheClass *newObject = [[TheClass alloc] init];
```

Do not override [`alloc`](./alloc.md) to include initialization code. Instead, implement class-specific versions of `init...` methods.

For historical reasons, [`alloc`](./alloc.md) invokes [`allocWithZone:`](./allocwithzone_.md).

## See Also

### Creating, Copying, and Deallocating Objects
- [+ allocWithZone:](./allocwithzone_.md)
  Returns a new instance of the receiving class.
- [init()](./init%28%29.md)
  Implemented by subclasses to initialize a new object (the receiver) immediately after memory for it has been allocated.
- [func copy() -> Any](./copy%28%29.md)
  Returns the object returned by `copy(with:)`.
- [+ copyWithZone:](./copywithzone_.md)
  Returns the receiver.
- [func mutableCopy() -> Any](./mutablecopy%28%29.md)
  Returns the object returned by `mutableCopy(with:)` where the zone is `nil`.
- [+ mutableCopyWithZone:](./mutablecopywithzone_.md)
  Returns the receiver.
- [- dealloc](./dealloc.md)
  Deallocates the memory occupied by the receiver.
- [+ new](./new.md)
  Allocates a new instance of the receiving class, sends it an [`init()`](./init%28%29.md) message, and returns the initialized object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/alloc)*