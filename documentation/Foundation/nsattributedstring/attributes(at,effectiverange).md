# attributes(at:effectiveRange:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSDictionary<NSString *,id> *) attributesAtIndex:(NSUInteger) location effectiveRange:(NSRangePointer) range;
```

## Return Value

The attributes for the character at `index`.

## Discussion

Raises an [`rangeException`](../nsexceptionname/rangeexception.md) if `index` lies beyond the end of the receiver’s characters.

For a list of possible attributes, see [`NSAttributedString.Key`](./key.md).

## Parameters

- `location`: The index for which to return attributes. This value must lie within the bounds of the receiver.
- `range`: Upon return, the range over which the attributes and values are the same as those at `index`. This range isn’t necessarily the maximum range covered, and its extent is implementation-dependent. If you need the maximum range, use [`attributes(at:longestEffectiveRange:in:)`](./attributes%28at,longesteffectiverange,in%29.md). If you don’t need this value, pass `NULL`.

## See Also

### Getting attributes for a range of text
- [func attributes(at: Int, longestEffectiveRange: NSRangePointer?, in: NSRange) -> [NSAttributedString.Key : Any]](./attributes%28at,longesteffectiverange,in%29.md)
  Returns the attributes for the character at the specified index and, by reference, the range where the attributes apply.
- [func attribute(NSAttributedString.Key, at: Int, effectiveRange: NSRangePointer?) -> Any?](./attribute%28_,at,effectiverange%29.md)
  Returns the value for an attribute with the specified name of the character at the specified index and, by reference, the range where the attribute applies.
- [func attribute(NSAttributedString.Key, at: Int, longestEffectiveRange: NSRangePointer?, in: NSRange) -> Any?](./attribute%28_,at,longesteffectiverange,in%29.md)
  Returns the value for the attribute with the specified name of the character at the specified index and, by reference, the range where the attribute applies.
- [func enumerateAttribute(NSAttributedString.Key, in: NSRange, options: NSAttributedString.EnumerationOptions, using: (Any?, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumerateattribute%28_,in,options,using%29.md)
  Executes the specified closure or block for each range of a particular attribute in the attributed string.
- [func enumerateAttributes(in: NSRange, options: NSAttributedString.EnumerationOptions, using: ([NSAttributedString.Key : Any], NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumerateattributes%28in,options,using%29.md)
  Executes the specified closure or block for each range of attributes in the attributed string.
- [NSAttributedString.EnumerationOptions](./enumerationoptions.md)
  Options for enumerating attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/attributes(at:effectiverange:))*