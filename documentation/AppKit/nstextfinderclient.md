# NSTextFinderClient

**Framework**: AppKit  
**Kind**: protocol

A set of methods implemented by objects that support searching using the [`NSTextFinder`](nstextfinder.md) class and the in-window text find bar.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSTextFinderClient : NSObjectProtocol
```

#### Overview

See [`NSTextFinder`](nstextfinder.md) for details.

## Topics

### String Searching
- [var string: String](nstextfinderclient/string.md)
  Allows the client to specify a single string for searching.
- [func string(at: Int, effectiveRange: NSRangePointer, endsWithSearchBoundary: UnsafeMutablePointer<ObjCBool>) -> String](nstextfinderclient/string(at:effectiverange:endswithsearchboundary:).md)
  Returns the found string that is created by conceptually mapping its content to a single string, which is composed of a concatenation of all its substrings.
- [func stringLength() -> Int](nstextfinderclient/stringlength.md)
  Returns the full length of the conceptually concatenated string return by the `stringAtIndex:effectiveRange:endsWithSearchBoundary:` method.
### Replacing Text
- [func shouldReplaceCharacters(inRanges: [NSValue], with: [String]) -> Bool](nstextfinderclient/shouldreplacecharacters(inranges:with:).md)
  Returns whether the specified strings should be replaced.
- [func replaceCharacters(in: NSRange, with: String)](nstextfinderclient/replacecharacters(in:with:).md)
  Replaces the text in the specified range with the new string.
- [func didReplaceCharacters()](nstextfinderclient/didreplacecharacters.md)
  Specifies whether text characters were replaced.
### Selection Information
- [var isSelectable: Bool](nstextfinderclient/isselectable.md)
  Returns whether the text is selectable.
- [var allowsMultipleSelection: Bool](nstextfinderclient/allowsmultipleselection.md)
  Returns whether multiple items can be selected.
- [var firstSelectedRange: NSRange](nstextfinderclient/firstselectedrange.md)
  Returns the currently selected range.
- [var selectedRanges: [NSValue]](nstextfinderclient/selectedranges.md)
  Returns an array of selected ranges.
### Text Edibility
- [var isEditable: Bool](nstextfinderclient/iseditable.md)
  Returns whether the text is editable.
### Determining and Displaying Text Locations
- [func contentView(at: Int, effectiveCharacterRange: NSRangePointer) -> NSView](nstextfinderclient/contentview(at:effectivecharacterrange:).md)
  Returns the view the context is displayed in.
- [func rects(forCharacterRange: NSRange) -> [NSValue]?](nstextfinderclient/rects(forcharacterrange:).md)
  An array containing the located text in the content view’s coordinate system.
- [func scrollRangeToVisible(NSRange)](nstextfinderclient/scrollrangetovisible(_:).md)
  Scrolls the specified range such that it is visible.
- [var visibleCharacterRanges: [NSValue]](nstextfinderclient/visiblecharacterranges.md)
  An array of visible character ranges.
### Drawing Glyphs
- [func drawCharacters(in: NSRange, forContentView: NSView)](nstextfinderclient/drawcharacters(in:forcontentview:).md)
  Draw the glyphs for the requested character range as they are drawn in the given content view.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSTextFinder](nstextfinder.md)
  An optional search-and-replace find interface inside a view, usually a scroll view.
- [protocol NSTextFinderBarContainer](nstextfinderbarcontainer.md)
  A protocol that provides a container in which the find bar is displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinderclient)*