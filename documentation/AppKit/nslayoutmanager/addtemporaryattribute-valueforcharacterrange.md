# addTemporaryAttribute(_:value:forCharacterRange:)

**Framework**: AppKit  
**Kind**: method

Adds a temporary attribute to the characters in the specified range.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func addTemporaryAttribute(_ attrName: NSAttributedString.Key, value: Any, forCharacterRange charRange: NSRange)
```

#### Discussion

Raises an [`invalidArgumentException`](https://developer.apple.com/documentation/Foundation/NSExceptionName/invalidArgumentException) if `attrName` or `value` is `nil`.

## Parameters

- `attrName`: The name of a temporary attribute.
- `value`: The temporary attribute value associated with  .
- `charRange`: The range of characters to which the specified attribute-value pair applies.

## See Also

- [func addTemporaryAttributes([NSAttributedString.Key : Any], forCharacterRange: NSRange)](nslayoutmanager/addtemporaryattributes(_:forcharacterrange:).md)
  Appends one or more temporary attributes to the attributes dictionary of the specified character range.
- [func setTemporaryAttributes([NSAttributedString.Key : Any], forCharacterRange: NSRange)](nslayoutmanager/settemporaryattributes(_:forcharacterrange:).md)
  Sets one or more temporary attributes for the specified character range.
- [func removeTemporaryAttribute(NSAttributedString.Key, forCharacterRange: NSRange)](nslayoutmanager/removetemporaryattribute(_:forcharacterrange:).md)
  Removes a temporary attribute from the list of attributes for the specified character range.
- [func temporaryAttribute(NSAttributedString.Key, atCharacterIndex: Int, effectiveRange: NSRangePointer?) -> Any?](nslayoutmanager/temporaryattribute(_:atcharacterindex:effectiverange:).md)
  Returns the value for the temporary attribute of a character, and the range it applies to.
- [func temporaryAttribute(NSAttributedString.Key, atCharacterIndex: Int, longestEffectiveRange: NSRangePointer?, in: NSRange) -> Any?](nslayoutmanager/temporaryattribute(_:atcharacterindex:longesteffectiverange:in:).md)
  Returns the value for the temporary attribute of a character, and the maximum range it applies to.
- [func temporaryAttributes(atCharacterIndex: Int, effectiveRange: NSRangePointer?) -> [NSAttributedString.Key : Any]](nslayoutmanager/temporaryattributes(atcharacterindex:effectiverange:).md)
  Returns the dictionary of temporary attributes for the specified character range.
- [func temporaryAttributes(atCharacterIndex: Int, longestEffectiveRange: NSRangePointer?, in: NSRange) -> [NSAttributedString.Key : Any]](nslayoutmanager/temporaryattributes(atcharacterindex:longesteffectiverange:in:).md)
  Returns the temporary attributes for a character, and the maximum range they apply to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/addtemporaryattribute(_:value:forcharacterrange:))*