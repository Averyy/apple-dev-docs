# CFArrayReleaseCallBack

**Framework**: Core Foundation  
**Kind**: typealias  
**Role**: Type Alias

Prototype of a callback function used to release a value before it’s removed from an array.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
typealias CFArrayReleaseCallBack = (CFAllocator?, UnsafeRawPointer?) -> Void
```

```c
typedef void (*)(const struct __CFAllocator *, const void *) CFArrayReleaseCallBack;
```

#### Discussion

This callback is passed to [`CFArrayCreate(_:_:_:_:)`](./cfarraycreate%28_,_,_,_%29.md) in a [`CFArrayCallBacks`](./cfarraycallbacks.md) structure.

## Parameters

- `allocator`: The array’s allocator.
- `value`: The value being removed from an array.

## See Also

### Callbacks
- [typealias CFArrayApplierFunction](./cfarrayapplierfunction.md)
  Prototype of a callback function that may be applied to every value in an array.
- [typealias CFArrayCopyDescriptionCallBack](./cfarraycopydescriptioncallback.md)
  Prototype of a callback function used to get a description of a value in an array.
- [typealias CFArrayEqualCallBack](./cfarrayequalcallback.md)
  Prototype of a callback function used to determine if two values in an array are equal.
- [typealias CFArrayRetainCallBack](./cfarrayretaincallback.md)
  Prototype of a callback function used to retain a value being added to an array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfarrayreleasecallback)*