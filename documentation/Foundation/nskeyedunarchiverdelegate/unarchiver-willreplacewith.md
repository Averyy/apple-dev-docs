# unarchiver(_:willReplace:with:)

**Framework**: Foundation  
**Kind**: method

Informs the delegate that one object is being substituted for another.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func unarchiver(_ unarchiver: NSKeyedUnarchiver, willReplace object: Any, with newObject: Any)
```

#### Discussion

This method is called even when the delegate itself is doing, or has done, the substitution with [`unarchiver(_:didDecode:)`](nskeyedunarchiverdelegate/unarchiver(_:diddecode:).md).

The delegate may use this method if it is keeping track of the encoded or decoded objects.

## Parameters

- `unarchiver`: An unarchiver for which the receiver is the delegate.
- `object`: An object in the archive.
- `newObject`: The object with which   will replace  .

## See Also

- [func unarchiver(NSKeyedUnarchiver, cannotDecodeObjectOfClassName: String, originalClasses: [String]) -> AnyClass?](nskeyedunarchiverdelegate/unarchiver(_:cannotdecodeobjectofclassname:originalclasses:).md)
  Informs the delegate that the class with a given name is not available during decoding.
- [func unarchiver(NSKeyedUnarchiver, didDecode: Any?) -> Any?](nskeyedunarchiverdelegate/unarchiver(_:diddecode:).md)
  Informs the delegate that a given object has been decoded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedunarchiverdelegate/unarchiver(_:willreplace:with:))*