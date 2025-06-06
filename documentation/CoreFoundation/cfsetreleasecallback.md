# CFSetReleaseCallBack

**Framework**: Core Foundation  
**Kind**: typealias

Prototype of a callback function used to release a value before it’s removed from a set.

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
typealias CFSetReleaseCallBack = (CFAllocator?, UnsafeRawPointer?) -> Void
```

#### Discussion

This callback is passed to [`CFSetCreate(_:_:_:_:)`](cfsetcreate(_:_:_:_:).md) in a [`CFSetCallBacks`](cfsetcallbacks.md) structure.

## Parameters

- `allocator`: The set’s allocator.
- `value`: The value being removed from the set.

## See Also

- [typealias CFSetApplierFunction](cfsetapplierfunction.md)
  Prototype of a callback function that may be applied to every value in a set.
- [typealias CFSetCopyDescriptionCallBack](cfsetcopydescriptioncallback.md)
  Prototype of a callback function used to get a description of a value in a set.
- [typealias CFSetEqualCallBack](cfsetequalcallback.md)
  Prototype of a callback function used to determine if two values in a set are equal.
- [typealias CFSetHashCallBack](cfsethashcallback.md)
  Prototype of a callback function called to compute a hash code for a value. Hash codes are used when values are accessed, added, or removed from a collection.
- [typealias CFSetRetainCallBack](cfsetretaincallback.md)
  Prototype of a callback function used to retain a value being added to a set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsetreleasecallback)*