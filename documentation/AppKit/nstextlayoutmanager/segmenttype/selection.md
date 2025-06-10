# NSTextLayoutManager.SegmentType.selection

**Framework**: AppKit  
**Kind**: case

The segment behavior suitable for selection rendering.

**Availability**:
- macOS 12.0+

## Declaration

```swift
case selection
```

#### Discussion

This segment type extends the last segment in a line fragment to the trailing edge if continuing to the next line.

## See Also

- [NSTextLayoutManager.SegmentType.highlight](nstextlayoutmanager/segmenttype/highlight.md)
  The segment behavior suitable for highlighting.
- [NSTextLayoutManager.SegmentType.standard](nstextlayoutmanager/segmenttype/standard.md)
  The standard segment, matching the typographic bounds of the range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutmanager/segmenttype/selection)*