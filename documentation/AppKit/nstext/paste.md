# paste(_:)

**Framework**: AppKit  
**Kind**: method

This action method pastes text from the general pasteboard at the insertion point or over the selection.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func paste(_ sender: Any?)
```

## See Also

- [func selectAll(Any?)](nstext/selectall(_:).md)
  This action method selects all of the receiver’s text.
- [func copy(Any?)](nstext/copy(_:).md)
  This action method copies the selected text onto the general pasteboard, in as many formats as the receiver supports.
- [func cut(Any?)](nstext/cut(_:).md)
  This action method deletes the selected text and places it onto the general pasteboard, in as many formats as the receiver supports.
- [func copyFont(Any?)](nstext/copyfont(_:).md)
  This action method copies the font information for the first character of the selection (or for the insertion point) onto the font pasteboard, as `NSFontPboardType`.
- [func pasteFont(Any?)](nstext/pastefont(_:).md)
  This action method pastes font information from the font pasteboard onto the selected text or insertion point of a rich text object, or over all text of a plain text object.
- [func copyRuler(Any?)](nstext/copyruler(_:).md)
  This action method copies the paragraph style information for first selected paragraph onto the ruler pasteboard, as `NSRulerPboardType`, and expands the selection to paragraph boundaries.
- [func pasteRuler(Any?)](nstext/pasteruler(_:).md)
  This action method pastes paragraph style information from the ruler pasteboard onto the selected paragraphs of a rich text object.
- [func delete(Any?)](nstext/delete(_:).md)
  This action method deletes the selected text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/paste(_:))*