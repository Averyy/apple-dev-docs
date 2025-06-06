# unarchiver(_:cannotDecodeObjectOfClassName:originalClasses:)

**Framework**: Foundation  
**Kind**: method

Informs the delegate that the class with a given name is not available during decoding.

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
optional func unarchiver(_ unarchiver: NSKeyedUnarchiver, cannotDecodeObjectOfClassName name: String, originalClasses classNames: [String]) -> AnyClass?
```

#### Return Value

The class unarchiver should use in place of the class named `name`.

#### Discussion

The delegate may, for example, load some code to introduce the class to the runtime and return the class, or substitute a different class object. If the delegate returns `nil`, unarchiving aborts and the method raises an `NSInvalidUnarchiveOperationException`.

## Parameters

- `unarchiver`: An unarchiver for which the receiver is the delegate.
- `name`: The name of the class of an object   is trying to decode.
- `classNames`: An array describing the class hierarchy of the encoded object, where the first element is the class name string of the encoded object, the second element is the class name of its immediate superclass, and so on.

## See Also

- [Archives and Serializations Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i)
- [func unarchiver(NSKeyedUnarchiver, didDecode: Any?) -> Any?](nskeyedunarchiverdelegate/unarchiver(_:diddecode:).md)
  Informs the delegate that a given object has been decoded.
- [func unarchiver(NSKeyedUnarchiver, willReplace: Any, with: Any)](nskeyedunarchiverdelegate/unarchiver(_:willreplace:with:).md)
  Informs the delegate that one object is being substituted for another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedunarchiverdelegate/unarchiver(_:cannotdecodeobjectofclassname:originalclasses:))*