# alignmentMode

**Framework**: Core Animation  
**Kind**: property

Determines how individual lines of text are horizontally aligned within the receiver’s bounds.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var alignmentMode: CATextLayerAlignmentMode { get set }
```

#### Discussion

The possible values are described in [`Horizontal alignment modes`](horizontal-alignment-modes.md). Defaults to [`natural`](catextlayeralignmentmode/natural.md).

## See Also

- [var isWrapped: Bool](catextlayer/iswrapped.md)
  Determines whether the text is wrapped to fit within the receiver’s bounds.
- [var truncationMode: CATextLayerTruncationMode](catextlayer/truncationmode.md)
  Determines how the text is truncated to fit within the receiver’s bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catextlayer/alignmentmode)*