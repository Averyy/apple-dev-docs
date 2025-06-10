# NSAccessibility.ParameterizedAttribute

**Framework**: AppKit  
**Kind**: struct

Values that describe parameterized attributes.

**Availability**:
- macOS ?+

## Declaration

```swift
struct ParameterizedAttribute
```

## Topics

### Attribute Names
- [static let attributedStringForRange: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/attributedstringforrange.md)
  Does not use attributes from Appkit/AttributedString.h (`NSAttributedString`).
- [static let boundsForRange: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/boundsforrange.md)
  The rectangle (`NSValue` containing an `NSRect` value) enclosing the specified range of characters (`NSValue` containing an `NSRange` value). If the range crosses a line boundary, the returned rectangle will fully enclose all the lines of characters.
- [static let cellForColumnAndRow: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/cellforcolumnandrow.md)
  The cell at the specified row and column.
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
- [static let styleRangeForIndex: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/stylerangeforindex.md)
  The full range of characters (`NSValue` containing an `NSRange` value), including the specified character (`NSNumber`), which have the same style.
- [static let uiElementsForSearchPredicateParameterizedAttribute: NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute/uielementsforsearchpredicateparameterizedattribute.md)
### Initializers
- [init(rawValue: String)](nsaccessibility-swift.struct/parameterizedattribute/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [NSAccessibility.Action](nsaccessibility-swift.struct/action.md)
  Constants that describe types of actions.
- [NSAccessibility.AnnotationAttributeKey](nsaccessibility-swift.struct/annotationattributekey.md)
  Keys for annotation attributes.
- [enum NSAccessibilityAnnotationPosition](nsaccessibilityannotationposition.md)
  Constants that specify the position where the annotation applies.
- [NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute.md)
  Constants that describe attributes.
- [NSAccessibility.FontAttributeKey](nsaccessibility-swift.struct/fontattributekey.md)
  Keys for font attributes.
- [enum NSAccessibilityOrientation](nsaccessibilityorientation.md)
  Values that indicate the orientation of accessibility elements, such as scroll bars and split views.
- [NSAccessibility.OrientationValue](nsaccessibility-swift.struct/orientationvalue.md)
  Values that indicate the orientation of user interface elements, such as scroll bars and split views.
- [NSAccessibility.Role](nsaccessibility-swift.struct/role.md)
  Values that describe types of objects that accessibility elements represent.
- [enum NSAccessibilityRulerMarkerType](nsaccessibilityrulermarkertype.md)
  Values that indicate the marker type of an accessibility element.
- [NSAccessibility.RulerMarkerTypeValue](nsaccessibility-swift.struct/rulermarkertypevalue.md)
  Values that describe ruler marker types.
- [NSAccessibility.RulerUnitValue](nsaccessibility-swift.struct/rulerunitvalue.md)
  Values that indicate the unit values of a ruler or layout area.
- [NSAccessibility.SortDirectionValue](nsaccessibility-swift.struct/sortdirectionvalue.md)
  Values that indicate the sort direction of a column.
- [enum NSAccessibilitySortDirection](nsaccessibilitysortdirection.md)
  Values that indicate the sort direction of a column.
- [NSAccessibility.Subrole](nsaccessibility-swift.struct/subrole.md)
  Values that describe specialized object subtypes that accessibility elements represent.
- [enum NSAccessibilityUnits](nsaccessibilityunits.md)
  Values that indicate the unit values of a ruler or layout area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/parameterizedattribute)*