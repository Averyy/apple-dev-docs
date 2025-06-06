# setTextColor(_:range:)

**Framework**: AppKit  
**Kind**: method

Sets the text color of characters within the specified range to the specified color.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setTextColor(_ color: NSColor?, range: NSRange)
```

#### Discussion

Removes the text color attribute if `color` is `nil`. This method applies only to rich text objects.

This method does not include undo support by default. Clients must invoke [`shouldChangeText(inRanges:replacementStrings:)`](nstextview/shouldchangetext(inranges:replacementstrings:).md) or [`shouldChangeText(in:replacementString:)`](nstextview/shouldchangetext(in:replacementstring:).md) to include this method in an undoable action.

## See Also

- [var textColor: NSColor?](nstext/textcolor.md)
  The text color of all characters in the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/settextcolor(_:range:))*