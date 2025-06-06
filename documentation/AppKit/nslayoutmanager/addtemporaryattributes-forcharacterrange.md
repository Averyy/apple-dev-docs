# addTemporaryAttributes(_:forCharacterRange:)

**Framework**: AppKit  
**Kind**: method

Appends one or more temporary attributes to the attributes dictionary of the specified character range.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func addTemporaryAttributes(_ attrs: [NSAttributedString.Key : Any] = [:], forCharacterRange charRange: NSRange)
```

#### Discussion

Temporary attributes are used only for onscreen drawing and are not persistent in any way. `NSTextView` uses them to color misspelled words when continuous spell checking is enabled. Currently the only temporary attributes recognized are those that do not affect layout (colors, underlines, and so on).

## Parameters

- `attrs`: Attributes dictionary containing the temporary attributes to add.
- `charRange`: The range of characters to which the specified attributes apply.

## See Also

- [func addTemporaryAttribute(NSAttributedString.Key, value: Any, forCharacterRange: NSRange)](nslayoutmanager/addtemporaryattribute(_:value:forcharacterrange:).md)
  Adds a temporary attribute to the characters in the specified range.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/addtemporaryattributes(_:forcharacterrange:))*