# NSAttributedString.EnumerationOptions

**Framework**: Foundation  
**Kind**: struct

Options for enumerating attributes.

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
struct EnumerationOptions
```

#### Overview

These constants describe the options available to the [`enumerateAttribute(_:in:options:using:)`](nsattributedstring/enumerateattribute(_:in:options:using:).md) and [`enumerateAttributes(in:options:using:)`](nsattributedstring/enumerateattributes(in:options:using:).md) methods.

## Topics

### Getting the enumeration options
- [static var reverse: NSAttributedString.EnumerationOptions](nsattributedstring/enumerationoptions/reverse.md)
  Causes the enumeration to occur in reverse.
- [static var longestEffectiveRangeNotRequired: NSAttributedString.EnumerationOptions](nsattributedstring/enumerationoptions/longesteffectiverangenotrequired.md)
  If `NSAttributedStringEnumerationLongestEffectiveRangeNotRequired` option is supplied, then the longest effective range computation is not performed; the blocks may be invoked with consecutive attribute runs that have the same value.
### Creating an enumeration option
- [init(rawValue: UInt)](nsattributedstring/enumerationoptions/init(rawvalue:).md)
- [static var reverse: NSAttributedString.EnumerationOptions](nsattributedstring/enumerationoptions/reverse.md)
  Causes the enumeration to occur in reverse.
- [static var longestEffectiveRangeNotRequired: NSAttributedString.EnumerationOptions](nsattributedstring/enumerationoptions/longesteffectiverangenotrequired.md)
  If `NSAttributedStringEnumerationLongestEffectiveRangeNotRequired` option is supplied, then the longest effective range computation is not performed; the blocks may be invoked with consecutive attribute runs that have the same value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func attributes(at: Int, effectiveRange: NSRangePointer?) -> [NSAttributedString.Key : Any]](nsattributedstring/attributes(at:effectiverange:).md)
  Returns the attributes for the character at the specified index.
- [func attributes(at: Int, longestEffectiveRange: NSRangePointer?, in: NSRange) -> [NSAttributedString.Key : Any]](nsattributedstring/attributes(at:longesteffectiverange:in:).md)
  Returns the attributes for the character at the specified index and, by reference, the range where the attributes apply.
- [func attribute(NSAttributedString.Key, at: Int, effectiveRange: NSRangePointer?) -> Any?](nsattributedstring/attribute(_:at:effectiverange:).md)
  Returns the value for an attribute with the specified name of the character at the specified index and, by reference, the range where the attribute applies.
- [func attribute(NSAttributedString.Key, at: Int, longestEffectiveRange: NSRangePointer?, in: NSRange) -> Any?](nsattributedstring/attribute(_:at:longesteffectiverange:in:).md)
  Returns the value for the attribute with the specified name of the character at the specified index and, by reference, the range where the attribute applies.
- [func enumerateAttribute(NSAttributedString.Key, in: NSRange, options: NSAttributedString.EnumerationOptions, using: (Any?, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](nsattributedstring/enumerateattribute(_:in:options:using:).md)
  Executes the specified closure or block for each range of a particular attribute in the attributed string.
- [func enumerateAttributes(in: NSRange, options: NSAttributedString.EnumerationOptions, using: ([NSAttributedString.Key : Any], NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](nsattributedstring/enumerateattributes(in:options:using:).md)
  Executes the specified closure or block for each range of attributes in the attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/enumerationoptions)*