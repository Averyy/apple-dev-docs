# CFArrayApplierFunction

**Framework**: Core Foundation  
**Kind**: typealias

Prototype of a callback function that may be applied to every value in an array.

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
typealias CFArrayApplierFunction = (UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Void
```

#### Discussion

This callback is passed to the [`CFArrayApplyFunction(_:_:_:_:)`](cfarrayapplyfunction(_:_:_:_:).md) function, which iterates over the values in an array and applies the behavior defined in the applier function to each value in an array.

## Parameters

- `value`: The current value in an array.
- `context`: The program-defined context parameter given to the applier   function.

## See Also

- [typealias CFArrayCopyDescriptionCallBack](cfarraycopydescriptioncallback.md)
  Prototype of a callback function used to get a description of a value in an array.
- [typealias CFArrayEqualCallBack](cfarrayequalcallback.md)
  Prototype of a callback function used to determine if two values in an array are equal.
- [typealias CFArrayReleaseCallBack](cfarrayreleasecallback.md)
  Prototype of a callback function used to release a value before it’s removed from an array.
- [typealias CFArrayRetainCallBack](cfarrayretaincallback.md)
  Prototype of a callback function used to retain a value being added to an array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfarrayapplierfunction)*