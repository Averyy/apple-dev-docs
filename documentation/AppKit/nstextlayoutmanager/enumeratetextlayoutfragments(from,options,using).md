# enumerateTextLayoutFragments(from:options:using:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Enumerates the text layout fragments starting at the specified location.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func enumerateTextLayoutFragments(from location: (any NSTextLocation)?, options: NSTextLayoutFragment.EnumerationOptions = [], using block: (NSTextLayoutFragment) -> Bool) -> (any NSTextLocation)?
```

```objc
- (id<NSTextLocation>) enumerateTextLayoutFragmentsFromLocation:(id<NSTextLocation>) location options:(NSTextLayoutFragmentEnumerationOptions) options usingBlock:(BOOL (^)(NSTextLayoutFragment *layoutFragment)) block;
```

## Return Value

An [`NSTextLocation`](../nstextlocation.md), or `nil`.

## Discussion

If `textLocation` is `nil`, the method starts at `self.textContentManager.documentRange.location`.The method uses `self.documentRange.endLocation` for reverse enumeration. When enumerating backward, it starts with the fragment preceding the one containing `textLocation`. If the method enumerates at least one fragment, it returns the edge of the enumerated range.

The enumerated range might not match the range of the last element returned; it enumerates the elements in the sequence, but it can skip a range. For example, it can limit the maximum number of text elements the method enumerates for a single invocation or hide some elements from the layout.

Returning `false` from `block` breaks out of the enumeration.

## Parameters

- `location`: The location where youstart the enumeration.
- `options`: One or more of the available [`NSTextLayoutFragment.EnumerationOptions`](../nstextlayoutfragment/enumerationoptions.md).
- `block`: A closure you provide that determines if the enumeration finishes early.

## See Also

### Causing layout generation
- [var textViewportLayoutController: NSTextViewportLayoutController](./textviewportlayoutcontroller.md)
  The text viewport layout controller associated with the layout manager’s text container.
- [func invalidateLayout(for: NSTextRange)](./invalidatelayout%28for%29.md)
  Invalidates the layout information for specified text range.
- [func textLayoutFragment(for: any NSTextLocation) -> NSTextLayoutFragment?](./textlayoutfragment%28for%29-68dez.md)
  Returns the text layout fragment from the document at the specified location.
- [func textLayoutFragment(for: CGPoint) -> NSTextLayoutFragment?](./textlayoutfragment%28for%29-4dhrx.md)
  Returns the text layout fragment at the position you specify in the text container.
- [func ensureLayout(for: CGRect)](./ensurelayout%28for%29-6ptsj.md)
  Performs the layout for filling the bounds you specify inside the last text container.
- [func ensureLayout(for: NSTextRange)](./ensurelayout%28for%29-3duae.md)
  Performs the layout for specified text range.
- [NSTextLayoutManager.SegmentType](./segmenttype.md)
  Values that describe the rendering of selection boundaries.
- [NSTextLayoutManager.SegmentOptions](./segmentoptions.md)
  Values that describe where and how the framework extends segments of a selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutmanager/enumeratetextlayoutfragments(from:options:using:))*