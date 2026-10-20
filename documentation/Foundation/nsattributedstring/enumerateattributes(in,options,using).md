# enumerateAttributes(in:options:using:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Executes the specified closure or block for each range of attributes in the attributed string.

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
func enumerateAttributes(in enumerationRange: NSRange, options opts: NSAttributedString.EnumerationOptions = [], using block: ([NSAttributedString.Key : Any], NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)
```

```objc
- (void) enumerateAttributesInRange:(NSRange) enumerationRange options:(NSAttributedStringEnumerationOptions) opts usingBlock:(void (^)(NSDictionary<NSString *,id> *attrs, NSRange range, BOOL *stop)) block;
```

#### Discussion

If this method is called by an instance of [`NSMutableAttributedString`](../nsmutableattributedstring.md), mutation (deletion, addition, or change) is allowed only if the mutation is within the range provided to the block. After a mutation, the enumeration continues with the range immediately following the processed range, adjusting for any change in length caused by the mutation. For example, if `block` is called with a range starting at location `N`, and the block deletes all the characters in the provided range, the next call will also pass `N` as the location of the range.

## Parameters

- `enumerationRange`: The range over which the attributes are enumerated.
- `opts`: The options used by the enumeration. For possible values, see [`NSAttributedString.EnumerationOptions`](./enumerationoptions.md).
- `block`: The closure or block to apply to ranges of attributes in the attributed string, taking three arguments:

  - A dictionary of attribute values keyed by name.
  - The range of the attribute values in the attributed string.
  - A reference to a Boolean value, which you can set to [`true`](../../Swift/true.md) within the closure to stop further processing of the attributed string.

## See Also

### Getting attributes for a range of text
- [func attributes(at: Int, effectiveRange: NSRangePointer?) -> [NSAttributedString.Key : Any]](./attributes%28at,effectiverange%29.md)
  Returns the attributes for the character at the specified index.
- [func attributes(at: Int, longestEffectiveRange: NSRangePointer?, in: NSRange) -> [NSAttributedString.Key : Any]](./attributes%28at,longesteffectiverange,in%29.md)
  Returns the attributes for the character at the specified index and, by reference, the range where the attributes apply.
- [func attribute(NSAttributedString.Key, at: Int, effectiveRange: NSRangePointer?) -> Any?](./attribute%28_,at,effectiverange%29.md)
  Returns the value for an attribute with the specified name of the character at the specified index and, by reference, the range where the attribute applies.
- [func attribute(NSAttributedString.Key, at: Int, longestEffectiveRange: NSRangePointer?, in: NSRange) -> Any?](./attribute%28_,at,longesteffectiverange,in%29.md)
  Returns the value for the attribute with the specified name of the character at the specified index and, by reference, the range where the attribute applies.
- [func enumerateAttribute(NSAttributedString.Key, in: NSRange, options: NSAttributedString.EnumerationOptions, using: (Any?, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumerateattribute%28_,in,options,using%29.md)
  Executes the specified closure or block for each range of a particular attribute in the attributed string.
- [NSAttributedString.EnumerationOptions](./enumerationoptions.md)
  Options for enumerating attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/enumerateattributes(in:options:using:))*