# kCMTextMarkupAttribute_TextPositionPercentageRelativeToWritingDirection

**Framework**: Core Media  
**Kind**: var

The placement of the block of text as a percentage in the writing direction.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
let kCMTextMarkupAttribute_TextPositionPercentageRelativeToWritingDirection: CFString
```

#### Discussion

This attribute’s value must be a non-negative `CFNumber` that expresses the position of the center of the text in the writing direction as a percentage of the video dimensions in the writing direction. For horizontal cues, this is the horizontal position. For vertical, it’s the vertical position. The system calculates the percentage from the edge of the frame where the text begins (for left-to-right English, it’s the left edge).

If you use this attribute, apply it to the entire attributed string.

## See Also

- [let kCMTextMarkupAttribute_VerticalLayout: CFString](kcmtextmarkupattribute_verticallayout.md)
  The vertical layout of a text block.
- [let kCMTextMarkupAttribute_Alignment: CFString](kcmtextmarkupattribute_alignment.md)
  The text alignment in the writing direction of the first line of text.
- [let kCMTextMarkupAttribute_OrthogonalLinePositionPercentageRelativeToWritingDirection: CFString](kcmtextmarkupattribute_orthogonallinepositionpercentagerelativetowritingdirection.md)
  The placement of the first line in a block of text as a percentage in the direction orthogonal to the writing direction.
- [let kCMTextMarkupAttribute_WritingDirectionSizePercentage: CFString](kcmtextmarkupattribute_writingdirectionsizepercentage.md)
  The width or height as a percentage of the bounding box that contains the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_textpositionpercentagerelativetowritingdirection)*