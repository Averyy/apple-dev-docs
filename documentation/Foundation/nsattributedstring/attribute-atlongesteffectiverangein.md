# attribute(_:at:longestEffectiveRange:in:)

**Framework**: Foundation  
**Kind**: method

Returns the value for the attribute with the specified name of the character at the specified index and, by reference, the range where the attribute applies.

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
func attribute(_ attrName: NSAttributedString.Key, at location: Int, longestEffectiveRange range: NSRangePointer?, in rangeLimit: NSRange) -> Any?
```

#### Return Value

The value for the attribute named `attributeName` of the character at `index`, or `nil` if there is no such attribute.

#### Discussion

Raises an [`rangeException`](nsexceptionname/rangeexception.md) if `index` or any part of `rangeLimit` lies beyond the end of the receiver’s characters.

If you don’t need the longest effective range, it’s far more efficient to use the [`attribute(_:at:effectiveRange:)`](nsattributedstring/attribute(_:at:effectiverange:).md) method to retrieve the attribute value.

For a list of possible attributes, see [`NSAttributedString.Key`](nsattributedstring/key.md).

## Parameters

- `attrName`: The name of an attribute.
- `location`: The index at which to test for  .
- `range`: If you don’t need this value, pass  .
- `rangeLimit`: The range over which to search for continuous presence of  . This value must not exceed the bounds of the receiver.

## See Also

- [func attributes(at: Int, effectiveRange: NSRangePointer?) -> [NSAttributedString.Key : Any]](nsattributedstring/attributes(at:effectiverange:).md)
  Returns the attributes for the character at the specified index.
- [func attributes(at: Int, longestEffectiveRange: NSRangePointer?, in: NSRange) -> [NSAttributedString.Key : Any]](nsattributedstring/attributes(at:longesteffectiverange:in:).md)
  Returns the attributes for the character at the specified index and, by reference, the range where the attributes apply.
- [func attribute(NSAttributedString.Key, at: Int, effectiveRange: NSRangePointer?) -> Any?](nsattributedstring/attribute(_:at:effectiverange:).md)
  Returns the value for an attribute with the specified name of the character at the specified index and, by reference, the range where the attribute applies.
- [func enumerateAttribute(NSAttributedString.Key, in: NSRange, options: NSAttributedString.EnumerationOptions, using: (Any?, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](nsattributedstring/enumerateattribute(_:in:options:using:).md)
  Executes the specified closure or block for each range of a particular attribute in the attributed string.
- [func enumerateAttributes(in: NSRange, options: NSAttributedString.EnumerationOptions, using: ([NSAttributedString.Key : Any], NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](nsattributedstring/enumerateattributes(in:options:using:).md)
  Executes the specified closure or block for each range of attributes in the attributed string.
- [NSAttributedString.EnumerationOptions](nsattributedstring/enumerationoptions.md)
  Options for enumerating attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/attribute(_:at:longesteffectiverange:in:))*