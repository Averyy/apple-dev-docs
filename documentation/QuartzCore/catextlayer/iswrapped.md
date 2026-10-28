# isWrapped

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

Determines whether the text is wrapped to fit within the receiver’s bounds.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var isWrapped: Bool { get set }
```

```objc
@property (getter=isWrapped) BOOL wrapped;
```

## Discussion

Defaults to [`false`](../../Swift/false.md).

## See Also

### Text Alignment and Truncation
- [var alignmentMode: CATextLayerAlignmentMode](./alignmentmode.md)
  Determines how individual lines of text are horizontally aligned within the receiver’s bounds.
- [var truncationMode: CATextLayerTruncationMode](./truncationmode.md)
  Determines how the text is truncated to fit within the receiver’s bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catextlayer/iswrapped)*