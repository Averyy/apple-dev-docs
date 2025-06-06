# showDefinition(for:range:options:baselineOriginProvider:)

**Framework**: AppKit  
**Kind**: method

Shows a window displaying the definition of the specified range of the attributed string.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
func showDefinition(for attrString: NSAttributedString?, range targetRange: NSRange, options: [NSView.DefinitionOptionKey : Any]? = nil, baselineOriginProvider originProvider: ((NSRange) -> NSPoint)? = nil)
```

#### Discussion

This method does not cause scrolling, so clients should perform any necessary scrolling before calling this method.

## Parameters

- `attrString`: The attributed string for which to show the definition. If the view is an instance of NSTextView, the   value can be  , in which case the text view will automatically supply values suitable for displaying definitions for the specified range within its text content.
- `targetRange`: The range of the attributed string to define. You can pass a zero-length range and the appropriate range will be auto-detected around the range’s offset.  That’s the recommended approach when there is no selection.
- `options`: An optional dictionary that specifies how the definition is displayed. See   for the key and it’s possible values.
- `originProvider`: The block object returns an   to be used as the baseline origin of the first character, in the view’s view coordinate system.

## See Also

- [func showDefinition(for: NSAttributedString?, at: NSPoint)](nsview/showdefinition(for:at:).md)
  Shows a window displaying the definition of the attributed string at the specified point.
- [NSView.DefinitionOptionKey](nsview/definitionoptionkey.md)
  Keys to include in your definition.
- [NSView.DefinitionPresentationType](nsview/definitionpresentationtype.md)
  Presentation options for the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/showdefinition(for:range:options:baselineoriginprovider:))*