# mutableCopy()

**Framework**: Objective-C Runtime  
**Kind**: method

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

#### Return Value

The object returned by the [`NSMutableCopying`](https://developer.apple.com/documentation/Foundation/NSMutableCopying) protocol method [`mutableCopy(with:)`](https://developer.apple.com/documentation/foundation/nsmutablecopying/1414175-mutablecopy), where the zone is `nil`.

#### Discussion

This is a convenience method for classes that adopt the [`NSMutableCopying`](https://developer.apple.com/documentation/Foundation/NSMutableCopying) protocol. An exception is raised if there is no implementation for [`mutableCopy(with:)`](https://developer.apple.com/documentation/foundation/nsmutablecopying/1414175-mutablecopy).

## See Also

- [init()](nsobject-swift.class/init.md)
  Implemented by subclasses to initialize a new object (the receiver) immediately after memory for it has been allocated.
- [func copy() -> Any](nsobject-swift.class/copy.md)
  Returns the object returned by `copy(with:)`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/mutablecopy())*