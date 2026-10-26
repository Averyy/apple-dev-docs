# copy()

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Returns the object returned by `copy(with:)`.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func copy() -> Any
```

```objc
- (id) copy;
```

#### Return Value

The object returned by the [`NSCopying`](../../Foundation/nscopying.md) protocol method [`copy(with:)`](../../Foundation/nscopying/copy%28with%29.md),.

#### Discussion

This is a convenience method for classes that adopt the [`NSCopying`](../../Foundation/nscopying.md) protocol. An exception is raised if there is no implementation for [`copy(with:)`](../../Foundation/nscopying/copy%28with%29.md).

`NSObject` does not itself support the [`NSCopying`](../../Foundation/nscopying.md) protocol. Subclasses must support the protocol and implement the [`copy(with:)`](../../Foundation/nscopying/copy%28with%29.md) method. A subclass version of the [`copy(with:)`](../../Foundation/nscopying/copy%28with%29.md) method should send the message to `super` first, to incorporate its implementation, unless the subclass descends directly from `NSObject`.

## See Also

### Creating, Copying, and Deallocating Objects
- [init()](./init%28%29.md)
  Implemented by subclasses to initialize a new object (the receiver) immediately after memory for it has been allocated.
- [func mutableCopy() -> Any](./mutablecopy%28%29.md)
  Returns the object returned by `mutableCopy(with:)` where the zone is `nil`.
- [+ alloc](./alloc.md)
  Returns a new instance of the receiving class.
- [+ allocWithZone:](./allocwithzone_.md)
  Returns a new instance of the receiving class.
- [+ copyWithZone:](./copywithzone_.md)
  Returns the receiver.
- [+ mutableCopyWithZone:](./mutablecopywithzone_.md)
  Returns the receiver.
- [- dealloc](./dealloc.md)
  Deallocates the memory occupied by the receiver.
- [+ new](./new.md)
  Allocates a new instance of the receiving class, sends it an [`init`](./init%28%29.md) message, and returns the initialized object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/copy())*