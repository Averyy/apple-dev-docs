# addTemporaryAttribute(_:value:forCharacterRange:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds a temporary attribute to the characters in the specified range.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func addTemporaryAttribute(_ attrName: NSAttributedString.Key, value: Any, forCharacterRange charRange: NSRange)
```

```objc
- (void) addTemporaryAttribute:(NSAttributedStringKey) attrName value:(id) value forCharacterRange:(NSRange) charRange;
```

## Discussion

Raises an [`invalidArgumentException`](../../Foundation/nsexceptionname/invalidargumentexception.md) if `attrName` or `value` is `nil`.

## Parameters

- `attrName`: The name of a temporary attribute.
- `value`: The temporary attribute value associated with `attrName`.
- `charRange`: The range of characters to which the specified attribute-value pair applies.

## See Also

### Managing temporary attribute support
- [func addTemporaryAttributes([NSAttributedString.Key : Any], forCharacterRange: NSRange)](./addtemporaryattributes%28_,forcharacterrange%29.md)
  Appends one or more temporary attributes to the attributes dictionary of the specified character range.
- [func setTemporaryAttributes([NSAttributedString.Key : Any], forCharacterRange: NSRange)](./settemporaryattributes%28_,forcharacterrange%29.md)
  Sets one or more temporary attributes for the specified character range.
- [func removeTemporaryAttribute(NSAttributedString.Key, forCharacterRange: NSRange)](./removetemporaryattribute%28_,forcharacterrange%29.md)
  Removes a temporary attribute from the list of attributes for the specified character range.
- [func temporaryAttribute(NSAttributedString.Key, atCharacterIndex: Int, effectiveRange: NSRangePointer?) -> Any?](./temporaryattribute%28_,atcharacterindex,effectiverange%29.md)
  Returns the value for the temporary attribute of a character, and the range it applies to.
- [func temporaryAttribute(NSAttributedString.Key, atCharacterIndex: Int, longestEffectiveRange: NSRangePointer?, in: NSRange) -> Any?](./temporaryattribute%28_,atcharacterindex,longesteffectiverange,in%29.md)
  Returns the value for the temporary attribute of a character, and the maximum range it applies to.
- [func temporaryAttributes(atCharacterIndex: Int, effectiveRange: NSRangePointer?) -> [NSAttributedString.Key : Any]](./temporaryattributes%28atcharacterindex,effectiverange%29.md)
  Returns the dictionary of temporary attributes for the specified character range.
- [func temporaryAttributes(atCharacterIndex: Int, longestEffectiveRange: NSRangePointer?, in: NSRange) -> [NSAttributedString.Key : Any]](./temporaryattributes%28atcharacterindex,longesteffectiverange,in%29.md)
  Returns the temporary attributes for a character, and the maximum range they apply to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/addtemporaryattribute(_:value:forcharacterrange:))*