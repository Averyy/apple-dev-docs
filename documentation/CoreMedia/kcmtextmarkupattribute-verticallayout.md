# kCMTextMarkupAttribute_VerticalLayout

**Framework**: Core Media  
**Kind**: var

The vertical layout of a text block.

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
let kCMTextMarkupAttribute_VerticalLayout: CFString
```

#### Discussion

Specifying this attribute indicates that the writing direction is vertical instead of horizontal. You can set the associated value to [`kCMTextVerticalLayout_LeftToRight`](kcmtextverticallayout_lefttoright.md) or [`kCMTextVerticalLayout_RightToLeft`](kcmtextverticallayout_righttoleft.md) to indicate the progression direction for new vertical lines of text.

## Topics

### Layouts
- [let kCMTextVerticalLayout_LeftToRight: CFString](kcmtextverticallayout_lefttoright.md)
  Add new vertical lines from left to right.
- [let kCMTextVerticalLayout_RightToLeft: CFString](kcmtextverticallayout_righttoleft.md)
  Add new vertical lines from right to left.

## See Also

- [let kCMTextMarkupAttribute_Alignment: CFString](kcmtextmarkupattribute_alignment.md)
  The text alignment in the writing direction of the first line of text.
- [let kCMTextMarkupAttribute_TextPositionPercentageRelativeToWritingDirection: CFString](kcmtextmarkupattribute_textpositionpercentagerelativetowritingdirection.md)
  The placement of the block of text as a percentage in the writing direction.
- [let kCMTextMarkupAttribute_OrthogonalLinePositionPercentageRelativeToWritingDirection: CFString](kcmtextmarkupattribute_orthogonallinepositionpercentagerelativetowritingdirection.md)
  The placement of the first line in a block of text as a percentage in the direction orthogonal to the writing direction.
- [let kCMTextMarkupAttribute_WritingDirectionSizePercentage: CFString](kcmtextmarkupattribute_writingdirectionsizepercentage.md)
  The width or height as a percentage of the bounding box that contains the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/kcmtextmarkupattribute_verticallayout)*