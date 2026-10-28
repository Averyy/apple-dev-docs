# temporaryAttribute(_:atCharacterIndex:longestEffectiveRange:in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the value for the temporary attribute of a character, and the maximum range it applies to.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func temporaryAttribute(_ attrName: NSAttributedString.Key, atCharacterIndex location: Int, longestEffectiveRange range: NSRangePointer?, in rangeLimit: NSRange) -> Any?
```

```objc
- (id) temporaryAttribute:(NSAttributedStringKey) attrName atCharacterIndex:(NSUInteger) location longestEffectiveRange:(NSRangePointer) range inRange:(NSRange) rangeLimit;
```

## Return Value

The value for the attribute named `attrName` of the character at `location`, or `nil` if there is no such attribute.

## Discussion

If you don’t need the longest effective range, it’s far more efficient to use the [`temporaryAttribute(_:atCharacterIndex:effectiveRange:)`](./temporaryattribute%28_,atcharacterindex,effectiverange%29.md) method to retrieve the attribute value.

## Parameters

- `attrName`: The name of a temporary attribute.
- `location`: The index for which to return attributes. This value must not exceed the bounds of the receiver.
- `range`: If non-`NULL`:

  - If the named attribute exists at `location`, on output, contains the maximum range over which the named attribute’s value applies, clipped to `rangeLimit`.
  - If the named attribute does not exist at `location`, on output, contains the maximum range over which the attribute does not exist.

  If you don’t need this value, pass `NULL`.
- `rangeLimit`: The range over which to search for continuous presence of `attrName`. This value must not exceed the bounds of the receiver.

## See Also

### Managing temporary attribute support
- [func addTemporaryAttributes([NSAttributedString.Key : Any], forCharacterRange: NSRange)](./addtemporaryattributes%28_,forcharacterrange%29.md)
  Appends one or more temporary attributes to the attributes dictionary of the specified character range.
- [func addTemporaryAttribute(NSAttributedString.Key, value: Any, forCharacterRange: NSRange)](./addtemporaryattribute%28_,value,forcharacterrange%29.md)
  Adds a temporary attribute to the characters in the specified range.
- [func setTemporaryAttributes([NSAttributedString.Key : Any], forCharacterRange: NSRange)](./settemporaryattributes%28_,forcharacterrange%29.md)
  Sets one or more temporary attributes for the specified character range.
- [func removeTemporaryAttribute(NSAttributedString.Key, forCharacterRange: NSRange)](./removetemporaryattribute%28_,forcharacterrange%29.md)
  Removes a temporary attribute from the list of attributes for the specified character range.
- [func temporaryAttribute(NSAttributedString.Key, atCharacterIndex: Int, effectiveRange: NSRangePointer?) -> Any?](./temporaryattribute%28_,atcharacterindex,effectiverange%29.md)
  Returns the value for the temporary attribute of a character, and the range it applies to.
- [func temporaryAttributes(atCharacterIndex: Int, effectiveRange: NSRangePointer?) -> [NSAttributedString.Key : Any]](./temporaryattributes%28atcharacterindex,effectiverange%29.md)
  Returns the dictionary of temporary attributes for the specified character range.
- [func temporaryAttributes(atCharacterIndex: Int, longestEffectiveRange: NSRangePointer?, in: NSRange) -> [NSAttributedString.Key : Any]](./temporaryattributes%28atcharacterindex,longesteffectiverange,in%29.md)
  Returns the temporary attributes for a character, and the maximum range they apply to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/temporaryattribute(_:atcharacterindex:longesteffectiverange:in:))*