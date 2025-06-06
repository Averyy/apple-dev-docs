# Text-Specific Parameterized Attributes

**Framework**: AppKit

Parameterized attributes specific to text.

## Topics

### Constants
- [static let lineForIndex: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/lineforindex.md)
  The line number (`NSNumber`) of the specified character (`NSNumber`).
- [static let rangeForLine: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/rangeforline.md)
  The range of characters (`NSValue` containing an `NSRange` value) corresponding to the specified line number (`NSNumber`).
- [static let stringForRange: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/stringforrange.md)
  The substring (`NSString`) specified by the range (`NSValue` containing an `NSRange` value).
- [static let rangeForPosition: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/rangeforposition.md)
  The range of characters (`NSValue` containing an `NSRange` value) composing the glyph at the specified point (`NSValue` containing an `NSPoint` value).
- [static let rangeForIndex: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/rangeforindex.md)
  The full range of characters (`NSValue` containing an `NSRange` value), including the specified character, which compose a single glyph (`NSNumber`).
- [static let boundsForRange: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/boundsforrange.md)
  The rectangle (`NSValue` containing an `NSRect` value) enclosing the specified range of characters (`NSValue` containing an `NSRange` value). If the range crosses a line boundary, the returned rectangle will fully enclose all the lines of characters.
- [static let rtfForRange: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/rtfforrange.md)
  The RTF data (`NSData`) describing the specified range of characters (`NSValue` containing an `NSRange` value).
- [static let styleRangeForIndex: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/stylerangeforindex.md)
  The full range of characters (`NSValue` containing an `NSRange` value), including the specified character (`NSNumber`), which have the same style.
- [static let attributedStringForRange: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/attributedstringforrange.md)
  Does not use attributes from Appkit/AttributedString.h (`NSAttributedString`).

## See Also

- [Standard Attributes](standard-attributes.md)
  Standard attributes that can be adopted by any accessibility object.
- [Text-Specific Attributes](text-specific-attributes.md)
  Attributes that are specific to text.
- [Text Attributed-String Attributes and Constants](text-attributed-string-attributes-and-constants.md)
  Attributes and key constants used with attributed strings.
- [Window-Specific Attributes](window-specific-attributes.md)
  Attributes specific to windows.
- [App-Specific Attributes](app-specific-attributes.md)
  Attributes that are specific to the app object.
- [Grid View Attributes](grid-view-attributes.md)
  Attributes that are used with grid views, such as thumbnails and media browsers that present a grid of items. The children of a grid are ordered.
- [Table View and Outline View Attributes](table-view-and-outline-view-attributes.md)
  Attributes that are specific to tables and outlines.
- [Outline View Attributes](outline-view-attributes.md)
  Attributes that are used in outline views.
- [Cell-Based Table Attributes](cell-based-table-attributes.md)
  Attributes that are specific to cell-based tables.
- [Cell-Based Table Parameterized Attributes](cell-based-table-parameterized-attributes.md)
  Parameterized attributes specific to cell-based tables.
- [Cell Attributes](cell-attributes.md)
  Attributes that are specific to individual table cells.
- [Layout Area Attributes](layout-area-attributes.md)
  Attributes that are specific to layout areas.
- [Layout Area Parameterized Attributes](layout-area-parameterized-attributes.md)
  Parameterized attributes that are specific to layout areas.
- [Layout Item Attributes](layout-item-attributes.md)
  Attributes that are specific to the items in a layout area.
- [Slider Attributes](slider-attributes.md)
  Attributes that are specific to sliders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/text-specific-parameterized-attributes)*