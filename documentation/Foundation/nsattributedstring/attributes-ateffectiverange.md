# attributes(at:effectiveRange:)

**Framework**: Foundation  
**Kind**: method

Returns the attributes for the character at the specified index.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func attributes(at location: Int, effectiveRange range: NSRangePointer?) -> [NSAttributedString.Key : Any]
```

#### Return Value

The attributes for the character at `index`.

#### Discussion

Raises an [`rangeException`](nsexceptionname/rangeexception.md) if `index` lies beyond the end of the receiver’s characters.

For a list of possible attributes, see [`NSAttributedString.Key`](nsattributedstring/key.md).

## Parameters

- `location`: The index for which to return attributes. This value must lie within the bounds of the receiver.
- `range`: Upon return, the range over which the attributes and values are the same as those at  . This range isn’t necessarily the maximum range covered, and its extent is implementation-dependent. If you need the maximum range, use  . If you don’t need this value, pass  .

## See Also

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
- [NSAttributedString.EnumerationOptions](nsattributedstring/enumerationoptions.md)
  Options for enumerating attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/attributes(at:effectiverange:))*