# copyWithZone:

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Type Method

Returns the receiver.

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
+ (id) copyWithZone:(struct _NSZone *) zone;
```

## Return Value

The receiver.

## Discussion

This method exists so class objects can be used in situations where you need an object that conforms to the [`NSCopying`](../../Foundation/nscopying.md) protocol. For example, this method lets you use a class object as a key to an `NSDictionary` object. You should not override this method.

## Parameters

- `zone`: This argument is ignored.

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
- [func mutableCopy() -> Any](./mutablecopy%28%29.md)
  Returns the object returned by `mutableCopy(with:)` where the zone is `nil`.
- [+ mutableCopyWithZone:](./mutablecopywithzone_.md)
  Returns the receiver.
- [- dealloc](./dealloc.md)
  Deallocates the memory occupied by the receiver.
- [+ new](./new.md)
  Allocates a new instance of the receiving class, sends it an [`init()`](./init%28%29.md) message, and returns the initialized object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/copywithzone:)*