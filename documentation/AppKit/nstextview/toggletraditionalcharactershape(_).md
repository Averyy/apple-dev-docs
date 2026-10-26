# toggleTraditionalCharacterShape(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Toggles the `NSCharacterShapeAttributeName` attribute at the current selection.

**Availability**:
- macOS 10.0+ - Deprecated in 10.11

> **Deprecated**: Use the traditional shaped characters encoded in the Unicode standard. Access the characters via the character palette.

## Declaration

```swift
func toggleTraditionalCharacterShape(_ sender: Any?)
```

```objc
- (void) toggleTraditionalCharacterShape:(id) sender;
```

#### Discussion

The `NSCharacterShapeAttributeName` constant is defined in NSAttributedString Application Kit Additions Reference.

## Parameters

- `sender`: The control that sent the message; may be `nil`.

## See Also

### Deprecated
- [func insertText(Any)](./inserttext%28_%29.md)
  Inserts `aString` into the receiver’s text at the insertion point if there is one, otherwise replacing the selection.
- [- toggleBaseWritingDirection:](./togglebasewritingdirection_.md)
  Changes the base writing direction of a paragraph between left-to-right and right-to-left.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/toggletraditionalcharactershape(_:))*