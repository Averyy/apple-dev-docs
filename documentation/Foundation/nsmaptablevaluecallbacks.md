# NSMapTableValueCallBacks

**Framework**: Foundation  
**Kind**: struct

The function pointers used to configure behavior of `NSMapTable` with respect to value elements within a map table.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct NSMapTableValueCallBacks
```

#### Overview

All functions must know the types of things in the map table to be able to operate on them. Sets of predefined call backs are described in [`NSMapTable`](nsmaptable.md).

## Topics

### Initializers
- [init()](nsmaptablevaluecallbacks/init.md)
- [init(retain: ((NSMapTable<AnyObject, AnyObject>, UnsafeRawPointer) -> Void)?, release: ((NSMapTable<AnyObject, AnyObject>, UnsafeMutableRawPointer) -> Void)?, describe: ((NSMapTable<AnyObject, AnyObject>, UnsafeRawPointer) -> String?)?)](nsmaptablevaluecallbacks/init(retain:release:describe:).md)
### Instance Properties
- [var describe: ((NSMapTable<AnyObject, AnyObject>, UnsafeRawPointer) -> String?)?](nsmaptablevaluecallbacks/describe.md)
  Points to the function that produces an autoreleased NSString * describing the given element. If `NULL`, then the map table produces a generic string description.
- [var release: ((NSMapTable<AnyObject, AnyObject>, UnsafeMutableRawPointer) -> Void)?](nsmaptablevaluecallbacks/release.md)
  Points to the function that decrements a reference count for the given element, and if the reference count becomes zero, frees the given element. If `NULL`, then nothing is done for reference counting or releasing.
- [var retain: ((NSMapTable<AnyObject, AnyObject>, UnsafeRawPointer) -> Void)?](nsmaptablevaluecallbacks/retain.md)
  Points to the function that increments a reference count for the given element. If `NULL`, then nothing is done for reference counting.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct NSMapEnumerator](nsmapenumerator.md)
  Allows successive elements of a map table to be returned each time this structure is passed to [`NSNextMapEnumeratorPair(_:_:_:)`](nsnextmapenumeratorpair(_:_:_:).md).
- [NSMapTable](legacy-nsmaptable.md)
  The opaque data type used by the functions described in Managing Map Tables.
- [struct NSMapTableKeyCallBacks](nsmaptablekeycallbacks.md)
  The function pointers used to configure behavior of `NSMapTable` with respect to key elements within a map table.
- [typealias NSMapTableOptions](nsmaptableoptions.md)
  Constants used as components in a bitfield to specify the behavior of elements (keys and values) in an `NSMapTable` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmaptablevaluecallbacks)*