# mutableCopy()

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Returns the object returned by `mutableCopy(with:)` where the zone is `nil`.

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
func mutableCopy() -> Any
```

```objc
- (id) mutableCopy;
```

#### Return Value

The object returned by the [`NSMutableCopying`](../../Foundation/nsmutablecopying.md) protocol method [`mutableCopy(with:)`](../../Foundation/nsmutablecopying/mutablecopy%28with%29.md), where the zone is `nil`.

#### Discussion

This is a convenience method for classes that adopt the [`NSMutableCopying`](../../Foundation/nsmutablecopying.md) protocol. An exception is raised if there is no implementation for [`mutableCopy(with:)`](../../Foundation/nsmutablecopying/mutablecopy%28with%29.md).

## See Also

### Creating, Copying, and Deallocating Objects
- [init()](./init%28%29.md)
  Implemented by subclasses to initialize a new object (the receiver) immediately after memory for it has been allocated.
- [func copy() -> Any](./copy%28%29.md)
  Returns the object returned by `copy(with:)`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/mutablecopy())*