# unarchiver(_:didDecode:)

**Framework**: Foundation  
**Kind**: method

Informs the delegate that a given object has been decoded.

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
optional func unarchiver(_ unarchiver: NSKeyedUnarchiver, didDecode object: Any?) -> Any?
```

#### Return Value

The object to use in place of `object`. The delegate can either return `object` or return a different object to replace the decoded one. In apps using ARC, the delegate should only return `nil` if `object` itself is `nil`. In apps not using ARC, the delegate can return `nil` to indicate that the decoded value is unchanged—that is, `object` will be decoded.

#### Discussion

This method is called after `object` has been sent [`init(coder:)`](https://developer.apple.com/documentation/OSLog/OSLogEntry/init(coder:)) and [`awakeAfter(using:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/awakeAfter(using:)).

The delegate may use this method to keep track of the decoded objects.

## Parameters

- `unarchiver`: An unarchiver for which the receiver is the delegate.
- `object`: The object that has been decoded.   may be  .

## See Also

- [func unarchiver(NSKeyedUnarchiver, cannotDecodeObjectOfClassName: String, originalClasses: [String]) -> AnyClass?](nskeyedunarchiverdelegate/unarchiver(_:cannotdecodeobjectofclassname:originalclasses:).md)
  Informs the delegate that the class with a given name is not available during decoding.
- [func unarchiver(NSKeyedUnarchiver, willReplace: Any, with: Any)](nskeyedunarchiverdelegate/unarchiver(_:willreplace:with:).md)
  Informs the delegate that one object is being substituted for another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedunarchiverdelegate/unarchiver(_:diddecode:))*