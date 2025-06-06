# textLineFragment(forVerticalOffset:requiresExactMatch:)

**Framework**: UIKit  
**Kind**: method

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

#### Return Value

A text line fragment, or `nil` if there isn’t a match.

#### Discussion

Set `requiresExactMatch` to [`true`](https://developer.apple.com/documentation/swift/true) to find the text line fragment that contains the vertical offset, or set `requiresExactMatch` to [`false`](https://developer.apple.com/documentation/swift/false) to find the closest text line fragment matching or beyond the vertical offset. Returns `nil` if there isn’t a match.

## Parameters

- `verticalOffset`: A float value that indicates a vertical distance, expressed in points, from the layout fragment frame’s origin.
- `requiresExactMatch`: A Boolean value that indicates whether the method returns an exact match, or returns the closest match if there isn’t an exact match. The default value is  .

## See Also

- [var textLineFragments: [NSTextLineFragment]](nstextlayoutfragment/textlinefragments.md)
  An array of text line fragments.
- [NSTextLayoutFragment.EnumerationOptions](nstextlayoutfragment/enumerationoptions.md)
  Values that describe options for enumerating text layout fragments.
- [func textLineFragment(for: any NSTextLocation, isUpstreamAffinity: Bool) -> NSTextLineFragment?](nstextlayoutfragment/textlinefragment(for:isupstreamaffinity:).md)
  Returns a text line fragment from a specific text location in the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlayoutfragment/textlinefragment(forverticaloffset:requiresexactmatch:))*