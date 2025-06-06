# textLayoutManager(_:shouldBreakLineBefore:hyphenating:)

**Framework**: UIKit  
**Kind**: method

The method the framework calls to determine the soft line break point.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
optional func textLayoutManager(_ textLayoutManager: NSTextLayoutManager, shouldBreakLineBefore location: any NSTextLocation, hyphenating: Bool) -> Bool
```

#### Return Value

A Boolean value that indicates if the framework should break the line at the current location.

#### Discussion

When `hyphenating` is `false`, `NSTextLayoutManager` tries to find the next line break opportunity before `location`. When `hyphenating` is `true`, it’s an auto-hyphenation point.

## Parameters

- `textLayoutManager`: The text layout manager.
- `location`: The location of the proposed line break.
- `hyphenating`: A Boolean value that indicates the current hyphenation mode.

## See Also

- [func textLayoutManager(NSTextLayoutManager, renderingAttributesForLink: Any, at: any NSTextLocation, defaultAttributes: [NSAttributedString.Key : Any]) -> [NSAttributedString.Key : Any]?](nstextlayoutmanagerdelegate/textlayoutmanager(_:renderingattributesforlink:at:defaultattributes:).md)
  The method the framework calls to return a dictionary of attributes for rendering a link attribute name.
- [func textLayoutManager(NSTextLayoutManager, textLayoutFragmentFor: any NSTextLocation, in: NSTextElement) -> NSTextLayoutFragment](nstextlayoutmanagerdelegate/textlayoutmanager(_:textlayoutfragmentfor:in:).md)
  The method the framework calls to give the delegate an opportunity to return a custom text layout fragment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlayoutmanagerdelegate/textlayoutmanager(_:shouldbreaklinebefore:hyphenating:))*