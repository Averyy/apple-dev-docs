# CFSetCopyDescriptionCallBack

**Framework**: Core Foundation  
**Kind**: typealias

Prototype of a callback function used to get a description of a value in a set.

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
typealias CFSetCopyDescriptionCallBack = (UnsafeRawPointer?) -> Unmanaged<CFString>?
```

#### Return Value

A textual description of `value`. The caller is responsible for releasing this object.

#### Discussion

This callback is passed to [`CFSetCreate(_:_:_:_:)`](cfsetcreate(_:_:_:_:).md) in a [`CFSetCallBacks`](cfsetcallbacks.md) structure. This callback is used by the [`CFCopyDescription(_:)`](cfcopydescription(_:).md) function.

## Parameters

- `value`: The value to be described.

## See Also

- [typealias CFSetApplierFunction](cfsetapplierfunction.md)
  Prototype of a callback function that may be applied to every value in a set.
- [typealias CFSetEqualCallBack](cfsetequalcallback.md)
  Prototype of a callback function used to determine if two values in a set are equal.
- [typealias CFSetHashCallBack](cfsethashcallback.md)
  Prototype of a callback function called to compute a hash code for a value. Hash codes are used when values are accessed, added, or removed from a collection.
- [typealias CFSetReleaseCallBack](cfsetreleasecallback.md)
  Prototype of a callback function used to release a value before it’s removed from a set.
- [typealias CFSetRetainCallBack](cfsetretaincallback.md)
  Prototype of a callback function used to retain a value being added to a set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsetcopydescriptioncallback)*