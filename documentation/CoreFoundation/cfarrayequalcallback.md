# CFArrayEqualCallBack

**Framework**: Core Foundation  
**Kind**: typealias

Prototype of a callback function used to determine if two values in an array are equal.

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
typealias CFArrayEqualCallBack = (UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean
```

#### Return Value

`true` if `value1` and `value2` are equal, `false` otherwise.

#### Discussion

This callback is passed to [`CFArrayCreate(_:_:_:_:)`](cfarraycreate(_:_:_:_:).md) in a [`CFArrayCallBacks`](cfarraycallbacks.md) structure.

## Parameters

- `value1`: A value in an array to be compared with   for equality.
- `value2`: A value in an array to be compared with   for equality.

## See Also

- [typealias CFArrayApplierFunction](cfarrayapplierfunction.md)
  Prototype of a callback function that may be applied to every value in an array.
- [typealias CFArrayCopyDescriptionCallBack](cfarraycopydescriptioncallback.md)
  Prototype of a callback function used to get a description of a value in an array.
- [typealias CFArrayReleaseCallBack](cfarrayreleasecallback.md)
  Prototype of a callback function used to release a value before it’s removed from an array.
- [typealias CFArrayRetainCallBack](cfarrayretaincallback.md)
  Prototype of a callback function used to retain a value being added to an array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfarrayequalcallback)*