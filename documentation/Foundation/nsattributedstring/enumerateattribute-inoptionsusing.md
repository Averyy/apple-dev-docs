# enumerateAttribute(_:in:options:using:)

**Framework**: Foundation  
**Kind**: method

Executes the specified closure or block for each range of a particular attribute in the attributed string.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func enumerateAttribute(_ attrName: NSAttributedString.Key, in enumerationRange: NSRange, options opts: NSAttributedString.EnumerationOptions = [], using block: (Any?, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)
```

#### Discussion

If this method is called by an instance of [`NSMutableAttributedString`](nsmutableattributedstring.md), mutation (deletion, addition, or change) is allowed only if the mutation is within the range provided to the block. After a mutation, the enumeration continues with the range immediately following the processed range, adjusting for any change in length caused by the mutation. For example, if `block` is called with a range starting at location `N`, and the block deletes all the characters in the provided range, the next call will also pass `N` as the location of the range.

## Parameters

- `attrName`: The name of the attribute to enumerate.
- `enumerationRange`: The range over which the attribute values are enumerated.
- `opts`: The options used by the enumeration. For possible values, see  .
- `block`: A closure or block to apply to ranges of the specified attribute in the attributed string, taking three arguments:

## See Also

- [func attributes(at: Int, effectiveRange: NSRangePointer?) -> [NSAttributedString.Key : Any]](nsattributedstring/attributes(at:effectiverange:).md)
  Returns the attributes for the character at the specified index.
- [func attributes(at: Int, longestEffectiveRange: NSRangePointer?, in: NSRange) -> [NSAttributedString.Key : Any]](nsattributedstring/attributes(at:longesteffectiverange:in:).md)
  Returns the attributes for the character at the specified index and, by reference, the range where the attributes apply.
- [func attribute(NSAttributedString.Key, at: Int, effectiveRange: NSRangePointer?) -> Any?](nsattributedstring/attribute(_:at:effectiverange:).md)
  Returns the value for an attribute with the specified name of the character at the specified index and, by reference, the range where the attribute applies.
- [func attribute(NSAttributedString.Key, at: Int, longestEffectiveRange: NSRangePointer?, in: NSRange) -> Any?](nsattributedstring/attribute(_:at:longesteffectiverange:in:).md)
  Returns the value for the attribute with the specified name of the character at the specified index and, by reference, the range where the attribute applies.
- [func enumerateAttributes(in: NSRange, options: NSAttributedString.EnumerationOptions, using: ([NSAttributedString.Key : Any], NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](nsattributedstring/enumerateattributes(in:options:using:).md)
  Executes the specified closure or block for each range of attributes in the attributed string.
- [NSAttributedString.EnumerationOptions](nsattributedstring/enumerationoptions.md)
  Options for enumerating attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/enumerateattribute(_:in:options:using:))*