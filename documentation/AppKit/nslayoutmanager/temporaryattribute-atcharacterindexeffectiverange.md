# temporaryAttribute(_:atCharacterIndex:effectiveRange:)

**Framework**: AppKit  
**Kind**: method

Returns the value for the temporary attribute of a character, and the range it applies to.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func temporaryAttribute(_ attrName: NSAttributedString.Key, atCharacterIndex location: Int, effectiveRange range: NSRangePointer?) -> Any?
```

#### Return Value

The value for the temporary attribute named `attrName` of the character at index `location`, or `nil` if there is no such attribute.

## Parameters

- `attrName`: The name of a temporary attribute.
- `location`: The index for which to return attributes. This value must not exceed the bounds of the receiver.
- `range`: The range isn’t necessarily the maximum range covered by  , and its extent is implementation-dependent. If you need the maximum range, use  . If you don’t need this value, pass  .

## See Also

- [func addTemporaryAttributes([NSAttributedString.Key : Any], forCharacterRange: NSRange)](nslayoutmanager/addtemporaryattributes(_:forcharacterrange:).md)
  Appends one or more temporary attributes to the attributes dictionary of the specified character range.
- [func addTemporaryAttribute(NSAttributedString.Key, value: Any, forCharacterRange: NSRange)](nslayoutmanager/addtemporaryattribute(_:value:forcharacterrange:).md)
  Adds a temporary attribute to the characters in the specified range.
- [func setTemporaryAttributes([NSAttributedString.Key : Any], forCharacterRange: NSRange)](nslayoutmanager/settemporaryattributes(_:forcharacterrange:).md)
  Sets one or more temporary attributes for the specified character range.
- [func removeTemporaryAttribute(NSAttributedString.Key, forCharacterRange: NSRange)](nslayoutmanager/removetemporaryattribute(_:forcharacterrange:).md)
  Removes a temporary attribute from the list of attributes for the specified character range.
- [func temporaryAttribute(NSAttributedString.Key, atCharacterIndex: Int, longestEffectiveRange: NSRangePointer?, in: NSRange) -> Any?](nslayoutmanager/temporaryattribute(_:atcharacterindex:longesteffectiverange:in:).md)
  Returns the value for the temporary attribute of a character, and the maximum range it applies to.
- [func temporaryAttributes(atCharacterIndex: Int, effectiveRange: NSRangePointer?) -> [NSAttributedString.Key : Any]](nslayoutmanager/temporaryattributes(atcharacterindex:effectiverange:).md)
  Returns the dictionary of temporary attributes for the specified character range.
- [func temporaryAttributes(atCharacterIndex: Int, longestEffectiveRange: NSRangePointer?, in: NSRange) -> [NSAttributedString.Key : Any]](nslayoutmanager/temporaryattributes(atcharacterindex:longesteffectiverange:in:).md)
  Returns the temporary attributes for a character, and the maximum range they apply to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/temporaryattribute(_:atcharacterindex:effectiverange:))*