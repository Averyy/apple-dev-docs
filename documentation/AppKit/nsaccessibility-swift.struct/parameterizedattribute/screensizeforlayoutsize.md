# screenSizeForLayoutSize

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The size of the screen in points (`NSValue`) corresponding to the specified size of the layout area (`NSValue`).

**Availability**:
- macOS 10.6+

## Declaration

```swift
static let screenSizeForLayoutSize: NSAccessibility.ParameterizedAttribute
```

```c
extern NSAccessibilityParameterizedAttributeName const NSAccessibilityScreenSizeForLayoutSizeParameterizedAttribute;
```

## See Also

### Attribute Names
- [static let attributedStringForRange: NSAccessibility.ParameterizedAttribute](./attributedstringforrange.md)
  Does not use attributes from Appkit/AttributedString.h (`NSAttributedString`).
- [static let boundsForRange: NSAccessibility.ParameterizedAttribute](./boundsforrange.md)
  The rectangle (`NSValue` containing an `NSRect` value) enclosing the specified range of characters (`NSValue` containing an `NSRange` value). If the range crosses a line boundary, the returned rectangle will fully enclose all the lines of characters.
- [static let cellForColumnAndRow: NSAccessibility.ParameterizedAttribute](./cellforcolumnandrow.md)
  The cell at the specified row and column.
- [static let indexForChildUIElementAttribute: NSAccessibility.ParameterizedAttribute](./indexforchilduielementattribute.md)
- [static let indexForChildUIElementInNavigationOrderAttribute: NSAccessibility.ParameterizedAttribute](./indexforchilduielementinnavigationorderattribute.md)
- [static let layoutPointForScreenPoint: NSAccessibility.ParameterizedAttribute](./layoutpointforscreenpoint.md)
  The point in the layout area (`NSValue`) corresponding to the specified point on the screen (`NSValue`).
- [static let layoutSizeForScreenSize: NSAccessibility.ParameterizedAttribute](./layoutsizeforscreensize.md)
  The size of the layout area in points (`NSValue`) corresponding to the specified screen size (`NSValue`).
- [static let lineForIndex: NSAccessibility.ParameterizedAttribute](./lineforindex.md)
  The line number (`NSNumber`) of the specified character (`NSNumber`).
- [static let rangeForIndex: NSAccessibility.ParameterizedAttribute](./rangeforindex.md)
  The full range of characters (`NSValue` containing an `NSRange` value), including the specified character, which compose a single glyph (`NSNumber`).
- [static let rangeForLine: NSAccessibility.ParameterizedAttribute](./rangeforline.md)
  The range of characters (`NSValue` containing an `NSRange` value) corresponding to the specified line number (`NSNumber`).
- [static let rangeForPosition: NSAccessibility.ParameterizedAttribute](./rangeforposition.md)
  The range of characters (`NSValue` containing an `NSRange` value) composing the glyph at the specified point (`NSValue` containing an `NSPoint` value).
- [static let resultsForSearchPredicateParameterizedAttribute: NSAccessibility.ParameterizedAttribute](./resultsforsearchpredicateparameterizedattribute.md)
- [static let rtfForRange: NSAccessibility.ParameterizedAttribute](./rtfforrange.md)
  The RTF data (`NSData`) describing the specified range of characters (`NSValue` containing an `NSRange` value).
- [static let screenPointForLayoutPoint: NSAccessibility.ParameterizedAttribute](./screenpointforlayoutpoint.md)
  The screen point (`NSValue`) corresponding to the specified point in the layout area (`NSValue`).
- [static let stringForRange: NSAccessibility.ParameterizedAttribute](./stringforrange.md)
  The substring (`NSString`) specified by the range (`NSValue` containing an `NSRange` value).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/parameterizedattribute/screensizeforlayoutsize)*