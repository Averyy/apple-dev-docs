# copy()

**Framework**: Objective-C Runtime  
**Kind**: method

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

#### Return Value

The object returned by the [`NSCopying`](https://developer.apple.com/documentation/Foundation/NSCopying) protocol method [`copy(with:)`](https://developer.apple.com/documentation/Foundation/NSCopying/copy(with:)),.

#### Discussion

This is a convenience method for classes that adopt the [`NSCopying`](https://developer.apple.com/documentation/Foundation/NSCopying) protocol. An exception is raised if there is no implementation for [`copy(with:)`](https://developer.apple.com/documentation/Foundation/NSCopying/copy(with:)).

`NSObject` does not itself support the [`NSCopying`](https://developer.apple.com/documentation/Foundation/NSCopying) protocol. Subclasses must support the protocol and implement the [`copy(with:)`](https://developer.apple.com/documentation/Foundation/NSCopying/copy(with:)) method. A subclass version of the [`copy(with:)`](https://developer.apple.com/documentation/Foundation/NSCopying/copy(with:)) method should send the message to `super` first, to incorporate its implementation, unless the subclass descends directly from `NSObject`.

## See Also

- [init()](nsobject-swift.class/init.md)
  Implemented by subclasses to initialize a new object (the receiver) immediately after memory for it has been allocated.
- [func mutableCopy() -> Any](nsobject-swift.class/mutablecopy.md)
  Returns the object returned by `mutableCopy(with:)` where the zone is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/copy())*