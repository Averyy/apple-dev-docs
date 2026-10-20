# textLineFragment(forVerticalOffset:requiresExactMatch:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the text line fragment for the vertical offset you provide, or the closest text line fragment beyond the vertical offset.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func textLineFragment(forVerticalOffset verticalOffset: CGFloat, requiresExactMatch: Bool) -> NSTextLineFragment?
```

```objc
- (NSTextLineFragment *) textLineFragmentForVerticalOffset:(CGFloat) verticalOffset requiresExactMatch:(BOOL) requiresExactMatch;
```

#### Return Value

A text line fragment, or `nil` if there isn’t a match.

#### Discussion

Set `requiresExactMatch` to [`true`](../../Swift/true.md) to find the text line fragment that contains the vertical offset, or set `requiresExactMatch` to [`false`](../../Swift/false.md) to find the closest text line fragment matching or beyond the vertical offset. Returns `nil` if there isn’t a match.

## Parameters

- `verticalOffset`: A float value that indicates a vertical distance, expressed in points, from the layout fragment frame’s origin.
- `requiresExactMatch`: A Boolean value that indicates whether the method returns an exact match, or returns the closest match if there isn’t an exact match. The default value is [`true`](../../Swift/true.md).

## See Also

### Getting line fragments
- [var textLineFragments: [NSTextLineFragment]](./textlinefragments.md)
  An array of text line fragments.
- [NSTextLayoutFragment.EnumerationOptions](./enumerationoptions.md)
  Values that describe options for enumerating text layout fragments.
- [func textLineFragment(for: any NSTextLocation, isUpstreamAffinity: Bool) -> NSTextLineFragment?](./textlinefragment%28for,isupstreamaffinity%29.md)
  Returns a text line fragment from a specific text location in the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlayoutfragment/textlinefragment(forverticaloffset:requiresexactmatch:))*