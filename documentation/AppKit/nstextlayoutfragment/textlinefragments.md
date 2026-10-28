# textLineFragments

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array of text line fragments.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var textLineFragments: [NSTextLineFragment] { get }
```

```objc
@property (copy, readonly) NSArray<NSTextLineFragment *> * textLineFragments;
```

## Discussion

Valid when [`NSTextLayoutFragment.State.layoutAvailable`](./state-swift.enum/layoutavailable.md). This property is KVO-compliant.

## See Also

### Getting line fragments
- [NSTextLayoutFragment.EnumerationOptions](./enumerationoptions.md)
  Values that describe options for enumerating text layout fragments.
- [func textLineFragment(for: any NSTextLocation, isUpstreamAffinity: Bool) -> NSTextLineFragment?](./textlinefragment%28for,isupstreamaffinity%29.md)
  Returns a text line fragment from a specific text location in the document.
- [func textLineFragment(forVerticalOffset: CGFloat, requiresExactMatch: Bool) -> NSTextLineFragment?](./textlinefragment%28forverticaloffset,requiresexactmatch%29.md)
  Returns the text line fragment for the vertical offset you provide, or the closest text line fragment beyond the vertical offset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutfragment/textlinefragments)*