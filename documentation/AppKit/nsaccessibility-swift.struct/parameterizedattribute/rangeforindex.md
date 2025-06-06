# rangeForIndex

**Framework**: AppKit  
**Kind**: property

The full range of characters (`NSValue` containing an `NSRange` value), including the specified character, which compose a single glyph (`NSNumber`).

**Availability**:
- macOS ?+

## Declaration

```swift
static let rangeForIndex: NSAccessibility.ParameterizedAttribute
```

## See Also

- [static let attributedStringForRange: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/attributedstringforrange.md)
  Does not use attributes from Appkit/AttributedString.h (`NSAttributedString`).
- [static let boundsForRange: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/boundsforrange.md)
  The rectangle (`NSValue` containing an `NSRect` value) enclosing the specified range of characters (`NSValue` containing an `NSRange` value). If the range crosses a line boundary, the returned rectangle will fully enclose all the lines of characters.
- [static let cellForColumnAndRow: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/cellforcolumnandrow.md)
  The cell at the specified row and column.
- [static let layoutPointForScreenPoint: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/layoutpointforscreenpoint.md)
  The point in the layout area (`NSValue`) corresponding to the specified point on the screen (`NSValue`).
- [static let layoutSizeForScreenSize: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/layoutsizeforscreensize.md)
  The size of the layout area in points (`NSValue`) corresponding to the specified screen size (`NSValue`).
- [static let lineForIndex: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/lineforindex.md)
  The line number (`NSNumber`) of the specified character (`NSNumber`).
- [static let rangeForLine: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/rangeforline.md)
  The range of characters (`NSValue` containing an `NSRange` value) corresponding to the specified line number (`NSNumber`).
- [static let rangeForPosition: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/rangeforposition.md)
  The range of characters (`NSValue` containing an `NSRange` value) composing the glyph at the specified point (`NSValue` containing an `NSPoint` value).
- [static let rtfForRange: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/rtfforrange.md)
  The RTF data (`NSData`) describing the specified range of characters (`NSValue` containing an `NSRange` value).
- [static let screenPointForLayoutPoint: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/screenpointforlayoutpoint.md)
  The screen point (`NSValue`) corresponding to the specified point in the layout area (`NSValue`).
- [static let screenSizeForLayoutSize: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/screensizeforlayoutsize.md)
  The size of the screen in points (`NSValue`) corresponding to the specified size of the layout area (`NSValue`).
- [static let stringForRange: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/stringforrange.md)
  The substring (`NSString`) specified by the range (`NSValue` containing an `NSRange` value).
- [static let styleRangeForIndex: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/stylerangeforindex.md)
  The full range of characters (`NSValue` containing an `NSRange` value), including the specified character (`NSNumber`), which have the same style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/parameterizedattribute/rangeforindex)*