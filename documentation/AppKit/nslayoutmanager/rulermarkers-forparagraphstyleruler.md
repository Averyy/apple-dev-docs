# rulerMarkers(for:paragraphStyle:ruler:)

**Framework**: AppKit  
**Kind**: method

Returns an array of text ruler objects for the current selection.

**Availability**:
- macOS ?+

## Declaration

```swift
func rulerMarkers(for view: NSTextView, paragraphStyle style: NSParagraphStyle, ruler: NSRulerView) -> [NSRulerMarker]
```

#### Return Value

An array of [`NSRulerMarker`](nsrulermarker.md) objects representing such things as left and right margins, first-line indent, and tab stops.

#### Discussion

If you have turned off automatic ruler updating through the use of [`usesRuler`](nstextview/usesruler.md) so that you can do more complex things, but you still want to display the appropriate accessory view, you can use this method.

This method is invoked automatically by the `NSTextView` object using the layout manager. You should rarely need to invoke it, but you can override it to add new kinds of markers or otherwise customize ruler support.

You can set the returned ruler markers with the `NSRulerView` method [`markers`](nsrulerview/markers.md).

## Parameters

- `view`: The text view using the layout manager.
- `style`: Sets the state of the controls in the accessory view; must not be  .
- `ruler`: The ruler view whose ruler markers are returned.

## See Also

- [func rulerAccessoryView(for: NSTextView, paragraphStyle: NSParagraphStyle, ruler: NSRulerView, enabled: Bool) -> NSView?](nslayoutmanager/ruleraccessoryview(for:paragraphstyle:ruler:enabled:).md)
  Returns the accessory view that the text system uses for its ruler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/rulermarkers(for:paragraphstyle:ruler:))*