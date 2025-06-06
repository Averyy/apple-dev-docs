# CFArrayRetainCallBack

**Framework**: Core Foundation  
**Kind**: typealias

Prototype of a callback function used to retain a value being added to an array.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
typealias CFArrayRetainCallBack = (CFAllocator?, UnsafeRawPointer?) -> UnsafeRawPointer?
```

#### Return Value

The value to store in an array, which is usually the `value` parameter passed to this callback, but may be a different   value if a different value should be stored in an array.

#### Discussion

This callback is passed to [`CFArrayCreate(_:_:_:_:)`](cfarraycreate(_:_:_:_:).md) in a [`CFArrayCallBacks`](cfarraycallbacks.md) structure.

## Parameters

- `allocator`: The array’s allocator.
- `value`: The value being added to an array.

## See Also

- [typealias CFArrayApplierFunction](cfarrayapplierfunction.md)
  Prototype of a callback function that may be applied to every value in an array.
- [typealias CFArrayCopyDescriptionCallBack](cfarraycopydescriptioncallback.md)
  Prototype of a callback function used to get a description of a value in an array.
- [typealias CFArrayEqualCallBack](cfarrayequalcallback.md)
  Prototype of a callback function used to determine if two values in an array are equal.
- [typealias CFArrayReleaseCallBack](cfarrayreleasecallback.md)
  Prototype of a callback function used to release a value before it’s removed from an array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfarrayretaincallback)*