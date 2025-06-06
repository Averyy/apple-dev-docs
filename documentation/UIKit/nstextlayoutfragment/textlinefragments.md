# textLineFragments

**Framework**: UIKit  
**Kind**: property

An array of text line fragments.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var textLineFragments: [NSTextLineFragment] { get }
```

#### Discussion

Valid when [`NSTextLayoutFragment.State.layoutAvailable`](nstextlayoutfragment/state-swift.enum/layoutavailable.md). This property is KVO-compliant.

## See Also

- [NSTextLayoutFragment.EnumerationOptions](nstextlayoutfragment/enumerationoptions.md)
  Values that describe options for enumerating text layout fragments.
- [func textLineFragment(for: any NSTextLocation, isUpstreamAffinity: Bool) -> NSTextLineFragment?](nstextlayoutfragment/textlinefragment(for:isupstreamaffinity:).md)
  Returns a text line fragment from a specific text location in the document.
- [func textLineFragment(forVerticalOffset: CGFloat, requiresExactMatch: Bool) -> NSTextLineFragment?](nstextlayoutfragment/textlinefragment(forverticaloffset:requiresexactmatch:).md)
  Returns the text line fragment for the vertical offset you provide, or the closest text line fragment beyond the vertical offset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlayoutfragment/textlinefragments)*