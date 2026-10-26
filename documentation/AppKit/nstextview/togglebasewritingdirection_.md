# toggleBaseWritingDirection:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Changes the base writing direction of a paragraph between left-to-right and right-to-left.

**Availability**:
- macOS 10.3+ - Deprecated in 10.6

> **Deprecated**: This method is deprecated in favor of the NSResponder class’s methods `makeBaseWritingDirectionNatural:`, `makeBaseWritingDirectionLeftToRight:`, and `makeBaseWritingDirectionRightToLeft:`.

## Declaration

```objc
- (void) toggleBaseWritingDirection:(id) sender;
```

## See Also

### Deprecated
- [func insertText(Any)](./inserttext%28_%29.md)
  Inserts `aString` into the receiver’s text at the insertion point if there is one, otherwise replacing the selection.
- [func toggleTraditionalCharacterShape(Any?)](./toggletraditionalcharactershape%28_%29.md)
  Toggles the `NSCharacterShapeAttributeName` attribute at the current selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/togglebasewritingdirection:)*