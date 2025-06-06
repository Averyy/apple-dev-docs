# replaceContents(in:with:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Replaces the characters specified by range with the text elements you provide.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func replaceContents(in range: NSTextRange, with textElements: [NSTextElement]?)
```

#### Discussion

If the edges of `range` aren’t at existing element range boundaries, the method either splits the element if it allows the operation (for example, [`NSTextParagraph`](nstextparagraph.md)), or the adjusts the replacement range.

> **Note**:  This method is for use by [`NSTextLayoutManager`](nstextlayoutmanager.md).

 This method is for use by [`NSTextLayoutManager`](nstextlayoutmanager.md).

## Parameters

- `range`: An  .
- `textElements`: The elements to replace that characters at  .

## See Also

- [func enumerateTextElements(from: (any NSTextLocation)?, options: NSTextContentManager.EnumerationOptions, using: (NSTextElement) -> Bool) -> (any NSTextLocation)?](nstextelementprovider/enumeratetextelements(from:options:using:).md)
  Enumerates text elements starting at the text location you provide.
- [NSTextLayoutFragment.EnumerationOptions](nstextlayoutfragment/enumerationoptions.md)
  Values that describe options for enumerating text layout fragments.
- [func location(any NSTextLocation, offsetBy: Int) -> (any NSTextLocation)?](nstextelementprovider/location(_:offsetby:).md)
  Returns a new location from location with offset you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextelementprovider/replacecontents(in:with:))*