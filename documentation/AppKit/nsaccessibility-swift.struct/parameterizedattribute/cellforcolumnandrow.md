# cellForColumnAndRow

**Framework**: AppKit  
**Kind**: property

The cell at the specified row and column.

**Availability**:
- macOS 10.6+

## Declaration

```swift
static let cellForColumnAndRow: NSAccessibility.ParameterizedAttribute
```

#### Discussion

The parameter is an `NSArray` that contains two `NSNumber` objects: the first number specifies the column index and the second number specifies the row index. This attribute is required for cell-based tables.

## See Also

- [static let attributedStringForRange: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/attributedstringforrange.md)
  Does not use attributes from Appkit/AttributedString.h (`NSAttributedString`).
- [static let boundsForRange: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/boundsforrange.md)
  The rectangle (`NSValue` containing an `NSRect` value) enclosing the specified range of characters (`NSValue` containing an `NSRange` value). If the range crosses a line boundary, the returned rectangle will fully enclose all the lines of characters.
- [static let indexForChildUIElementAttribute: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/indexforchilduielementattribute.md)
- [static let indexForChildUIElementInNavigationOrderAttribute: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/indexforchilduielementinnavigationorderattribute.md)
- [static let layoutPointForScreenPoint: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/layoutpointforscreenpoint.md)
  The point in the layout area (`NSValue`) corresponding to the specified point on the screen (`NSValue`).
- [static let layoutSizeForScreenSize: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/layoutsizeforscreensize.md)
  The size of the layout area in points (`NSValue`) corresponding to the specified screen size (`NSValue`).
- [static let lineForIndex: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/lineforindex.md)
  The line number (`NSNumber`) of the specified character (`NSNumber`).
- [static let rangeForIndex: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/rangeforindex.md)
  The full range of characters (`NSValue` containing an `NSRange` value), including the specified character, which compose a single glyph (`NSNumber`).
- [static let rangeForLine: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/rangeforline.md)
  The range of characters (`NSValue` containing an `NSRange` value) corresponding to the specified line number (`NSNumber`).
- [static let rangeForPosition: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/rangeforposition.md)
  The range of characters (`NSValue` containing an `NSRange` value) composing the glyph at the specified point (`NSValue` containing an `NSPoint` value).
- [static let resultsForSearchPredicateParameterizedAttribute: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/resultsforsearchpredicateparameterizedattribute.md)
- [static let rtfForRange: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/rtfforrange.md)
  The RTF data (`NSData`) describing the specified range of characters (`NSValue` containing an `NSRange` value).
- [static let screenPointForLayoutPoint: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/screenpointforlayoutpoint.md)
  The screen point (`NSValue`) corresponding to the specified point in the layout area (`NSValue`).
- [static let screenSizeForLayoutSize: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/screensizeforlayoutsize.md)
  The size of the screen in points (`NSValue`) corresponding to the specified size of the layout area (`NSValue`).
- [static let stringForRange: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/stringforrange.md)
  The substring (`NSString`) specified by the range (`NSValue` containing an `NSRange` value).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/parameterizedattribute/cellforcolumnandrow)*