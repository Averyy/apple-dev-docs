# setTextColor(_:range:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the text color of characters within the specified range to the specified color.

**Availability**:
- macOS

## Declaration

```swift
func setTextColor(_ color: NSColor?, range: NSRange)
```

```objc
- (void) setTextColor:(NSColor *) color range:(NSRange) range;
```

## Discussion

Removes the text color attribute if `color` is `nil`. This method applies only to rich text objects.

This method does not include undo support by default. Clients must invoke [`shouldChangeText(inRanges:replacementStrings:)`](../nstextview/shouldchangetext%28inranges,replacementstrings%29.md) or [`shouldChangeText(in:replacementString:)`](../nstextview/shouldchangetext%28in,replacementstring%29.md) to include this method in an undoable action.

## See Also

### Setting text color
- [var textColor: NSColor?](./textcolor.md)
  The text color of all characters in the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/settextcolor(_:range:))*