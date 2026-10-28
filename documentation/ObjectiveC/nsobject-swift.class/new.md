# new

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Type Method

Allocates a new instance of the receiving class, sends it an [`init()`](./init%28%29.md) message, and returns the initialized object.

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
+ (instancetype) new;
```

## Return Value

A new instance of the receiver.

## Discussion

This method is a combination of [`alloc`](./alloc.md) and [`init()`](./init%28%29.md). Like [`alloc`](./alloc.md), it initializes the `isa` instance variable of the new object so it points to the class data structure. It then invokes the [`init()`](./init%28%29.md) method to complete the initialization process.

## See Also

### Creating, Copying, and Deallocating Objects
- [+ alloc](./alloc.md)
  Returns a new instance of the receiving class.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/new)*