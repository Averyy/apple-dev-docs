# CFBagReleaseCallBack

**Framework**: Core Foundation  
**Kind**: typealias

Prototype of a callback function used to release a value before it’s removed from a bag.

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
typealias CFBagReleaseCallBack = (CFAllocator?, UnsafeRawPointer?) -> Void
```

#### Discussion

This callback is passed to [`CFBagCreate(_:_:_:_:)`](cfbagcreate(_:_:_:_:).md) in a [`CFBagCallBacks`](cfbagcallbacks.md) structure.

## Parameters

- `allocator`: The bag’s allocator.
- `value`: The value being removed from the bag.

## See Also

- [typealias CFBagApplierFunction](cfbagapplierfunction.md)
  Prototype of a callback function that may be applied to every value in a bag.
- [typealias CFBagCopyDescriptionCallBack](cfbagcopydescriptioncallback.md)
  Prototype of a callback function used to get a description of a value in a bag.
- [typealias CFBagEqualCallBack](cfbagequalcallback.md)
  Prototype of a callback function used to determine if two values in a bag are equal.
- [typealias CFBagHashCallBack](cfbaghashcallback.md)
  Prototype of a callback function invoked to compute a hash code for a value. Hash codes are used when values are accessed, added, or removed from a collection.
- [typealias CFBagRetainCallBack](cfbagretaincallback.md)
  Prototype of a callback function used to retain a value being added to a bag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbagreleasecallback)*