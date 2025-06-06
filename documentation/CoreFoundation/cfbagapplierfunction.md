# CFBagApplierFunction

**Framework**: Core Foundation  
**Kind**: typealias

Prototype of a callback function that may be applied to every value in a bag.

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
typealias CFBagApplierFunction = (UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Void
```

#### Discussion

This callback is passed to the [`CFBagApplyFunction(_:_:_:)`](cfbagapplyfunction(_:_:_:).md) function which iterates over the values in a bag and applies the behavior defined in the applier function to each value in a bag.

## Parameters

- `value`: The current value in a bag.
- `context`: The program-defined context parameter given to the apply   function.

## See Also

- [typealias CFBagCopyDescriptionCallBack](cfbagcopydescriptioncallback.md)
  Prototype of a callback function used to get a description of a value in a bag.
- [typealias CFBagEqualCallBack](cfbagequalcallback.md)
  Prototype of a callback function used to determine if two values in a bag are equal.
- [typealias CFBagHashCallBack](cfbaghashcallback.md)
  Prototype of a callback function invoked to compute a hash code for a value. Hash codes are used when values are accessed, added, or removed from a collection.
- [typealias CFBagReleaseCallBack](cfbagreleasecallback.md)
  Prototype of a callback function used to release a value before it’s removed from a bag.
- [typealias CFBagRetainCallBack](cfbagretaincallback.md)
  Prototype of a callback function used to retain a value being added to a bag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbagapplierfunction)*