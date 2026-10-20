# textLineFragment(for:isUpstreamAffinity:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a text line fragment from a specific text location in the document.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func textLineFragment(for textLocation: any NSTextLocation, isUpstreamAffinity: Bool) -> NSTextLineFragment?
```

```objc
- (NSTextLineFragment *) textLineFragmentForTextLocation:(id<NSTextLocation>) textLocation isUpstreamAffinity:(BOOL) isUpstreamAffinity;
```

#### Return Value

The text line fragment that contains or ends at the text location you provide, or `nil` if there isn’t a match.

#### Discussion

Set `isUpstreamAffinity` to [`true`](../../Swift/true.md) to find a text fragment by its element range end location, such as when you enumerate over line fragments in reverse order. Set `isUpstreamAffinity` to [`false`](../../Swift/false.md) to find a text fragment that contains `textLocation`.

## Parameters

- `textLocation`: A text location that a text line fragment contains.
- `isUpstreamAffinity`: A Boolean value that indicates whether the text line fragment ends at the text location you provide.

## See Also

### Getting line fragments
- [var textLineFragments: [NSTextLineFragment]](./textlinefragments.md)
  An array of text line fragments.
- [NSTextLayoutFragment.EnumerationOptions](./enumerationoptions.md)
  Values that describe options for enumerating text layout fragments.
- [func textLineFragment(forVerticalOffset: CGFloat, requiresExactMatch: Bool) -> NSTextLineFragment?](./textlinefragment%28forverticaloffset,requiresexactmatch%29.md)
  Returns the text line fragment for the vertical offset you provide, or the closest text line fragment beyond the vertical offset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutfragment/textlinefragment(for:isupstreamaffinity:))*