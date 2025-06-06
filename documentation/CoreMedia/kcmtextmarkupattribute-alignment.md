# kCMTextMarkupAttribute_Alignment

**Framework**: Core Media  
**Kind**: var

The text alignment in the writing direction of the first line of text.

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
let kCMTextMarkupAttribute_Alignment: CFString
```

#### Discussion

This attribute’s value must be one of the constants listed below that indicate the alignment in the writing direction of the first line of text of the cue. The value (or absence) of the [`kCMTextMarkupAttribute_VerticalLayout`](kcmtextmarkupattribute_verticallayout.md) attribute indicates the writing direction. The default value of this attribute is [`kCMTextMarkupAlignmentType_Middle`](kcmtextmarkupalignmenttype_middle.md).

If you use this attribute, apply it to the entire attributed string.

## Topics

### Alignment Types
- [let kCMTextMarkupAlignmentType_Start: CFString](kcmtextmarkupalignmenttype_start.md)
  An alignment type that visually aligns the text at its starting side.
- [let kCMTextMarkupAlignmentType_Middle: CFString](kcmtextmarkupalignmenttype_middle.md)
  An alignment type that visually aligns text in the center between its starting and ending sides.
- [let kCMTextMarkupAlignmentType_End: CFString](kcmtextmarkupalignmenttype_end.md)
  An alignment type that visually aligns the text at its ending side.
- [let kCMTextMarkupAlignmentType_Left: CFString](kcmtextmarkupalignmenttype_left.md)
  An alignment type that visually aligns text from left-to-right.
- [let kCMTextMarkupAlignmentType_Right: CFString](kcmtextmarkupalignmenttype_right.md)
  An alignment type that visually aligns text from right-to-left.

## See Also

- [let kCMTextMarkupAttribute_VerticalLayout: CFString](kcmtextmarkupattribute_verticallayout.md)
  The vertical layout of a text block.
- [let kCMTextMarkupAttribute_TextPositionPercentageRelativeToWritingDirection: CFString](kcmtextmarkupattribute_textpositionpercentagerelativetowritingdirection.md)
  The placement of the block of text as a percentage in the writing direction.
- [let kCMTextMarkupAttribute_OrthogonalLinePositionPercentageRelativeToWritingDirection: CFString](kcmtextmarkupattribute_orthogonallinepositionpercentagerelativetowritingdirection.md)
  The placement of the first line in a block of text as a percentage in the direction orthogonal to the writing direction.
- [let kCMTextMarkupAttribute_WritingDirectionSizePercentage: CFString](kcmtextmarkupattribute_writingdirectionsizepercentage.md)
  The width or height as a percentage of the bounding box that contains the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_alignment)*