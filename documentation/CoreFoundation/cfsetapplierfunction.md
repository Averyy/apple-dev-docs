# CFSetApplierFunction

**Framework**: Core Foundation  
**Kind**: typealias

Prototype of a callback function that may be applied to every value in a set.

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
typealias CFSetApplierFunction = (UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Void
```

#### Discussion

This callback is passed to the [`CFSetApplyFunction(_:_:_:)`](cfsetapplyfunction(_:_:_:).md) function which iterates over the values in a set and applies the behavior defined in the applier function to each value in a set.

## Parameters

- `value`: The current value in a set.
- `context`: The program-defined context parameter given to the apply function.

## See Also

- [typealias CFSetCopyDescriptionCallBack](cfsetcopydescriptioncallback.md)
  Prototype of a callback function used to get a description of a value in a set.
- [typealias CFSetEqualCallBack](cfsetequalcallback.md)
  Prototype of a callback function used to determine if two values in a set are equal.
- [typealias CFSetHashCallBack](cfsethashcallback.md)
  Prototype of a callback function called to compute a hash code for a value. Hash codes are used when values are accessed, added, or removed from a collection.
- [typealias CFSetReleaseCallBack](cfsetreleasecallback.md)
  Prototype of a callback function used to release a value before it’s removed from a set.
- [typealias CFSetRetainCallBack](cfsetretaincallback.md)
  Prototype of a callback function used to retain a value being added to a set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsetapplierfunction)*