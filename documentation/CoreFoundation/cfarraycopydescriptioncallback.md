# CFArrayCopyDescriptionCallBack

**Framework**: Core Foundation  
**Kind**: typealias  
**Role**: Type Alias

Prototype of a callback function used to get a description of a value in an array.

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
typealias CFArrayCopyDescriptionCallBack = (UnsafeRawPointer?) -> Unmanaged<CFString>?
```

```c
typedef const struct __CFString *(*)(const void *) CFArrayCopyDescriptionCallBack;
```

#### Return Value

A textual description of `value`. The caller is responsible for releasing this object.

#### Discussion

This callback is passed to [`CFArrayCreate(_:_:_:_:)`](./cfarraycreate%28_,_,_,_%29.md) in a [`CFArrayCallBacks`](./cfarraycallbacks.md) structure. This callback is used by the [`CFCopyDescription(_:)`](./cfcopydescription%28_%29.md) function.

## Parameters

- `value`: The value to be described.

## See Also

### Callbacks
- [typealias CFArrayApplierFunction](./cfarrayapplierfunction.md)
  Prototype of a callback function that may be applied to every value in an array.
- [typealias CFArrayEqualCallBack](./cfarrayequalcallback.md)
  Prototype of a callback function used to determine if two values in an array are equal.
- [typealias CFArrayReleaseCallBack](./cfarrayreleasecallback.md)
  Prototype of a callback function used to release a value before it’s removed from an array.
- [typealias CFArrayRetainCallBack](./cfarrayretaincallback.md)
  Prototype of a callback function used to retain a value being added to an array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfarraycopydescriptioncallback)*