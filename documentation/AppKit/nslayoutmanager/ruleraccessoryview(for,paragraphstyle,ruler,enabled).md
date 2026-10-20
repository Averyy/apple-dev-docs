# rulerAccessoryView(for:paragraphStyle:ruler:enabled:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the accessory view that the text system uses for its ruler.

**Availability**:
- macOS

## Declaration

```swift
func rulerAccessoryView(for view: NSTextView, paragraphStyle style: NSParagraphStyle, ruler: NSRulerView, enabled isEnabled: Bool) -> NSView?
```

```objc
- (NSView *) rulerAccessoryViewForTextView:(NSTextView *) view paragraphStyle:(NSParagraphStyle *) style ruler:(NSRulerView *) ruler enabled:(BOOL) isEnabled;
```

#### Return Value

The accessory view containing tab wells, text alignment buttons, and so on.

#### Discussion

If you have turned off automatic ruler updating through the use of [`usesRuler`](../nstextview/usesruler.md) so that you can do more complex things, but you still want to display the appropriate accessory view, you can use this method.

This method is invoked automatically by the [`NSTextView`](../nstextview.md) object using the layout manager. You should rarely need to invoke it, but you can override it to customize ruler support. If you do use this method directly, note that it neither installs the ruler accessory view nor sets the markers for the [`NSRulerView`](../nsrulerview.md) object. You must install the accessory view into the ruler using the [`NSRulerView`](../nsrulerview.md) method [`accessoryView`](../nsrulerview/accessoryview.md). To set the markers, use [`rulerMarkers(for:paragraphStyle:ruler:)`](./rulermarkers%28for,paragraphstyle,ruler%29.md) to get the markers needed, and then send [`markers`](../nsrulerview/markers.md) to the ruler.

## Parameters

- `view`: The text view using the layout manager.
- `style`: Sets the state of the controls in the accessory view; must not be `nil`.
- `ruler`: The ruler view whose accessory view is returned.
- `isEnabled`: If [`true`](../../Swift/true.md), the accessory view is enabled and accepts mouse and keyboard events; if [`false`](../../Swift/false.md) it’s disabled.

## See Also

### Handling Rulers
- [func rulerMarkers(for: NSTextView, paragraphStyle: NSParagraphStyle, ruler: NSRulerView) -> [NSRulerMarker]](./rulermarkers%28for,paragraphstyle,ruler%29.md)
  Returns an array of text ruler objects for the current selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/ruleraccessoryview(for:paragraphstyle:ruler:enabled:))*