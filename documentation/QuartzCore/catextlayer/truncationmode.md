# truncationMode

**Framework**: Core Animation  
**Kind**: property

Determines how the text is truncated to fit within the receiver’s bounds.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var truncationMode: CATextLayerTruncationMode { get set }
```

#### Discussion

The possible values are described in [`Truncation modes`](truncation-modes.md). Defaults to [`none`](catextlayertruncationmode/none.md).

## See Also

- [var isWrapped: Bool](catextlayer/iswrapped.md)
  Determines whether the text is wrapped to fit within the receiver’s bounds.
- [var alignmentMode: CATextLayerAlignmentMode](catextlayer/alignmentmode.md)
  Determines how individual lines of text are horizontally aligned within the receiver’s bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catextlayer/truncationmode)*