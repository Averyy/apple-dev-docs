# allocWithZone:

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
+ (instancetype) allocWithZone:(struct _NSZone *) zone;
```

#### Return Value

A new instance of the receiver.

#### Discussion

The `isa` instance variable of the new instance is initialized to a data structure that describes the class; memory for all other instance variables is set to `0`.

You must use an `init...` method to complete the initialization process. For example:

```objc
TheClass *newObject = [[TheClass allocWithZone:nil] init];
```

Do not override [`allocWithZone:`](./allocwithzone_.md) to include any initialization code. Instead, class-specific versions of `init...` methods.

This method exists for historical reasons; memory zones are no longer used by Objective-C.

## Parameters

- `zone`: This parameter is ignored.

## See Also

### Creating, Copying, and Deallocating Objects
- [+ alloc](./alloc.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/allocwithzone:)*