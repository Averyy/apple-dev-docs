# delete(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

This action method deletes the selected text.

**Availability**:
- macOS

## Declaration

```swift
func delete(_ sender: Any?)
```

```objc
- (void) delete:(id) sender;
```

## See Also

### Action methods for editing
- [func selectAll(Any?)](./selectall%28_%29.md)
  This action method selects all of the receiver’s text.
- [func copy(Any?)](./copy%28_%29.md)
  This action method copies the selected text onto the general pasteboard, in as many formats as the receiver supports.
- [func cut(Any?)](./cut%28_%29.md)
  This action method deletes the selected text and places it onto the general pasteboard, in as many formats as the receiver supports.
- [func paste(Any?)](./paste%28_%29.md)
  This action method pastes text from the general pasteboard at the insertion point or over the selection.
- [func copyFont(Any?)](./copyfont%28_%29.md)
  This action method copies the font information for the first character of the selection (or for the insertion point) onto the font pasteboard, as `NSFontPboardType`.
- [func pasteFont(Any?)](./pastefont%28_%29.md)
  This action method pastes font information from the font pasteboard onto the selected text or insertion point of a rich text object, or over all text of a plain text object.
- [func copyRuler(Any?)](./copyruler%28_%29.md)
  This action method copies the paragraph style information for first selected paragraph onto the ruler pasteboard, as `NSRulerPboardType`, and expands the selection to paragraph boundaries.
- [func pasteRuler(Any?)](./pasteruler%28_%29.md)
  This action method pastes paragraph style information from the ruler pasteboard onto the selected paragraphs of a rich text object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstext/delete(_:))*