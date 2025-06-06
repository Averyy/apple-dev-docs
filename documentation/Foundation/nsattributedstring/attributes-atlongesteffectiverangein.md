# attributes(at:longestEffectiveRange:in:)

**Framework**: Foundation  
**Kind**: method

Returns the attributes for the character at the specified index and, by reference, the range where the attributes apply.

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
func attributes(at location: Int, longestEffectiveRange range: NSRangePointer?, in rangeLimit: NSRange) -> [NSAttributedString.Key : Any]
```

#### Discussion

Raises an [`rangeException`](nsexceptionname/rangeexception.md) if `index` or any part of `rangeLimit` lies beyond the end of the receiver’s characters.

If you don’t need the range information, it’s far more efficient to use the [`attributes(at:effectiveRange:)`](nsattributedstring/attributes(at:effectiverange:).md) method to retrieve the attribute value.

For a list of possible attributes, see [`NSAttributedString.Key`](nsattributedstring/key.md).

## Parameters

- `location`: The index for which to return attributes. This value must not exceed the bounds of the receiver.
- `range`: If non- , upon return contains the maximum range over which the attributes and values are the same as those at  , clipped to  .
- `rangeLimit`: The range over which to search for continuous presence of the attributes at  . This value must not exceed the bounds of the receiver.

## See Also

- [func attributes(at: Int, effectiveRange: NSRangePointer?) -> [NSAttributedString.Key : Any]](nsattributedstring/attributes(at:effectiverange:).md)
  Returns the attributes for the character at the specified index.
- [func attribute(NSAttributedString.Key, at: Int, effectiveRange: NSRangePointer?) -> Any?](nsattributedstring/attribute(_:at:effectiverange:).md)
  Returns the value for an attribute with the specified name of the character at the specified index and, by reference, the range where the attribute applies.
- [func attribute(NSAttributedString.Key, at: Int, longestEffectiveRange: NSRangePointer?, in: NSRange) -> Any?](nsattributedstring/attribute(_:at:longesteffectiverange:in:).md)
  Returns the value for the attribute with the specified name of the character at the specified index and, by reference, the range where the attribute applies.
- [func enumerateAttribute(NSAttributedString.Key, in: NSRange, options: NSAttributedString.EnumerationOptions, using: (Any?, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](nsattributedstring/enumerateattribute(_:in:options:using:).md)
  Executes the specified closure or block for each range of a particular attribute in the attributed string.
- [func enumerateAttributes(in: NSRange, options: NSAttributedString.EnumerationOptions, using: ([NSAttributedString.Key : Any], NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](nsattributedstring/enumerateattributes(in:options:using:).md)
  Executes the specified closure or block for each range of attributes in the attributed string.
- [NSAttributedString.EnumerationOptions](nsattributedstring/enumerationoptions.md)
  Options for enumerating attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/attributes(at:longesteffectiverange:in:))*