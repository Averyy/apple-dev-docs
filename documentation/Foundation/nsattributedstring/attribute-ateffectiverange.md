# attribute(_:at:effectiveRange:)

**Framework**: Foundation  
**Kind**: method

Returns the value for an attribute with the specified name of the character at the specified index and, by reference, the range where the attribute applies.

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
func attribute(_ attrName: NSAttributedString.Key, at location: Int, effectiveRange range: NSRangePointer?) -> Any?
```

#### Return Value

The value for the attribute named `attrName` of the character at `location`, or `nil` if there is no such attribute.

#### Discussion

For a list of possible attributes, see [`NSAttributedString.Key`](nsattributedstring/key.md).

## Parameters

- `attrName`: The name of an attribute.
- `location`: The index for which to return attributes. This value must not exceed the bounds of the receiver. > ❗ **Important**:  Raises an [`rangeException`](nsexceptionname/rangeexception.md) if `index` lies beyond the end of the receiver’s characters.
- `range`: If non-`NULL`: - If the named attribute exists at `index`, upon return `aRange` contains a range over which the named attribute’s value applies.
- If the named attribute does not exist at `index`, upon return `aRange` contains the range over which the attribute does not exist. The range isn’t necessarily the maximum range covered by `attributeName`, and its extent is implementation-dependent. If you need the maximum range, use [`attribute(_:at:longestEffectiveRange:in:)`](nsattributedstring/attribute(_:at:longesteffectiverange:in:).md). If you don’t need this value, pass `NULL`.

## See Also

- [func attributes(at: Int, effectiveRange: NSRangePointer?) -> [NSAttributedString.Key : Any]](nsattributedstring/attributes(at:effectiverange:).md)
  Returns the attributes for the character at the specified index.
- [func attributes(at: Int, longestEffectiveRange: NSRangePointer?, in: NSRange) -> [NSAttributedString.Key : Any]](nsattributedstring/attributes(at:longesteffectiverange:in:).md)
  Returns the attributes for the character at the specified index and, by reference, the range where the attributes apply.
- [func attribute(NSAttributedString.Key, at: Int, longestEffectiveRange: NSRangePointer?, in: NSRange) -> Any?](nsattributedstring/attribute(_:at:longesteffectiverange:in:).md)
  Returns the value for the attribute with the specified name of the character at the specified index and, by reference, the range where the attribute applies.
- [func enumerateAttribute(NSAttributedString.Key, in: NSRange, options: NSAttributedString.EnumerationOptions, using: (Any?, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](nsattributedstring/enumerateattribute(_:in:options:using:).md)
  Executes the specified closure or block for each range of a particular attribute in the attributed string.
- [func enumerateAttributes(in: NSRange, options: NSAttributedString.EnumerationOptions, using: ([NSAttributedString.Key : Any], NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](nsattributedstring/enumerateattributes(in:options:using:).md)
  Executes the specified closure or block for each range of attributes in the attributed string.
- [NSAttributedString.EnumerationOptions](nsattributedstring/enumerationoptions.md)
  Options for enumerating attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/attribute(_:at:effectiverange:))*