# NSTextLayoutManager.SegmentType.selection

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

The segment behavior suitable for selection rendering.

**Availability**:
- macOS 12.0+

## Declaration

```swift
case selection
```

```c
NSTextLayoutManagerSegmentTypeSelection
```

#### Discussion

This segment type extends the last segment in a line fragment to the trailing edge if continuing to the next line.

## See Also

### Kinds of text selection segments
- [NSTextLayoutManager.SegmentType.highlight](./highlight.md)
  The segment behavior suitable for highlighting.
- [NSTextLayoutManager.SegmentType.standard](./standard.md)
  The standard segment, matching the typographic bounds of the range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlayoutmanager/segmenttype/selection)*