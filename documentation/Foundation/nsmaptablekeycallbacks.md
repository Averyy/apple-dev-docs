# NSMapTableKeyCallBacks

**Framework**: Foundation  
**Kind**: struct

The function pointers used to configure behavior of `NSMapTable` with respect to key elements within a map table.

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
struct NSMapTableKeyCallBacks
```

#### Overview

All functions must know the types of things in the map table to be able to operate on them. Sets of predefined call backs are described in [`NSMapTable`](nsmaptable.md).

Two predefined values to use for `notAKeyMarker` are [`NSNotAnIntMapKey`](nsnotanintmapkey.md) and [`NSNotAPointerMapKey`](nsnotapointermapkey.md).

## Topics

### Initializers
- [init()](nsmaptablekeycallbacks/init.md)
- [init(hash: ((NSMapTable<AnyObject, AnyObject>, UnsafeRawPointer) -> Int)?, isEqual: ((NSMapTable<AnyObject, AnyObject>, UnsafeRawPointer, UnsafeRawPointer) -> ObjCBool)?, retain: ((NSMapTable<AnyObject, AnyObject>, UnsafeRawPointer) -> Void)?, release: ((NSMapTable<AnyObject, AnyObject>, UnsafeMutableRawPointer) -> Void)?, describe: ((NSMapTable<AnyObject, AnyObject>, UnsafeRawPointer) -> String?)?, notAKeyMarker: UnsafeRawPointer?)](nsmaptablekeycallbacks/init(hash:isequal:retain:release:describe:notakeymarker:).md)
### Instance Properties
- [var describe: ((NSMapTable<AnyObject, AnyObject>, UnsafeRawPointer) -> String?)?](nsmaptablekeycallbacks/describe.md)
  Points to the function which produces an autoreleased NSString * describing the given element. If `NULL`, then the map table produces a generic string description.
- [var hash: ((NSMapTable<AnyObject, AnyObject>, UnsafeRawPointer) -> Int)?](nsmaptablekeycallbacks/hash.md)
  Points to the function which must produce hash code for key elements of the map table. If `NULL`, the pointer value is used as the hash code. Second parameter is the element for which hash code should be produced.
- [var isEqual: ((NSMapTable<AnyObject, AnyObject>, UnsafeRawPointer, UnsafeRawPointer) -> ObjCBool)?](nsmaptablekeycallbacks/isequal.md)
  Points to the function which compares second and third parameters. If `NULL`, then == is used for comparison.
- [var notAKeyMarker: UnsafeRawPointer?](nsmaptablekeycallbacks/notakeymarker.md)
  No key put in map table can be this value. An exception is raised if attempt is made to use this value as a key
- [var release: ((NSMapTable<AnyObject, AnyObject>, UnsafeMutableRawPointer) -> Void)?](nsmaptablekeycallbacks/release.md)
  Points to the function which decrements a reference count for the given element, and if the reference count becomes zero, frees the given element. If `NULL`, then nothing is done for reference counting or releasing.
- [var retain: ((NSMapTable<AnyObject, AnyObject>, UnsafeRawPointer) -> Void)?](nsmaptablekeycallbacks/retain.md)
  Points to the function which increments a reference count for the given element. If `NULL`, then nothing is done for reference counting.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct NSMapEnumerator](nsmapenumerator.md)
  Allows successive elements of a map table to be returned each time this structure is passed to [`NSNextMapEnumeratorPair(_:_:_:)`](nsnextmapenumeratorpair(_:_:_:).md).
- [NSMapTable](legacy-nsmaptable.md)
  The opaque data type used by the functions described in Managing Map Tables.
- [typealias NSMapTableOptions](nsmaptableoptions.md)
  Constants used as components in a bitfield to specify the behavior of elements (keys and values) in an `NSMapTable` object.
- [struct NSMapTableValueCallBacks](nsmaptablevaluecallbacks.md)
  The function pointers used to configure behavior of `NSMapTable` with respect to value elements within a map table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmaptablekeycallbacks)*