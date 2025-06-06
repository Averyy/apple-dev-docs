# CFBagCopyDescriptionCallBack

**Framework**: Core Foundation  
**Kind**: typealias

Prototype of a callback function used to get a description of a value in a bag.

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
typealias CFBagCopyDescriptionCallBack = (UnsafeRawPointer?) -> Unmanaged<CFString>?
```

#### Return Value

A textual description of `value`. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

This callback is passed to [`CFBagCreate(_:_:_:_:)`](cfbagcreate(_:_:_:_:).md) in a [`CFBagCallBacks`](cfbagcallbacks.md) structure. This callback is used by the [`CFCopyDescription(_:)`](cfcopydescription(_:).md) function.

## Parameters

- `value`: The value to be described.

## See Also

- [typealias CFBagApplierFunction](cfbagapplierfunction.md)
  Prototype of a callback function that may be applied to every value in a bag.
- [typealias CFBagEqualCallBack](cfbagequalcallback.md)
  Prototype of a callback function used to determine if two values in a bag are equal.
- [typealias CFBagHashCallBack](cfbaghashcallback.md)
  Prototype of a callback function invoked to compute a hash code for a value. Hash codes are used when values are accessed, added, or removed from a collection.
- [typealias CFBagReleaseCallBack](cfbagreleasecallback.md)
  Prototype of a callback function used to release a value before it’s removed from a bag.
- [typealias CFBagRetainCallBack](cfbagretaincallback.md)
  Prototype of a callback function used to retain a value being added to a bag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbagcopydescriptioncallback)*