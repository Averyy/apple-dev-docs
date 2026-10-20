# none

**Framework**: Core Animation  
**Kind**: property  
**Role**: Type Property

Each line is displayed so that the text is either wrapped or clipped.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static let none: CATextLayerTruncationMode
```

```c
extern CATextLayerTruncationMode const kCATruncationNone;
```

#### Discussion

If the [`isWrapped`](../catextlayer/iswrapped.md) property is [`true`](../../Swift/true.md), the text is wrapped to the receiver’s bounds, otherwise the text is clipped to the receiver’s bounds.

## See Also

### Constants
- [static let start: CATextLayerTruncationMode](./start.md)
  Each line is displayed so that the end fits in the container and the missing text is indicated by some kind of ellipsis glyph.
- [static let end: CATextLayerTruncationMode](./end.md)
  Each line is displayed so that the beginning fits in the container and the missing text is indicated by some kind of ellipsis glyph.
- [static let middle: CATextLayerTruncationMode](./middle.md)
  Each line is displayed so that the beginning and end fit in the container and the missing text is indicated by some kind of ellipsis glyph in the middle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catextlayertruncationmode/none)*