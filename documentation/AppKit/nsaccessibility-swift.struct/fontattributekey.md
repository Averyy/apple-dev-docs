# NSAccessibility.FontAttributeKey

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Keys for font attributes.

**Availability**:
- macOS

## Declaration

```swift
struct FontAttributeKey
```

```c
typedef NSString * NSAccessibilityFontAttributeKey;
```

## Topics

### Font Attributes
- [static let fontFamily: NSAccessibility.FontAttributeKey](./fontattributekey/fontfamily.md)
  An optional key for a font family.
- [static let fontName: NSAccessibility.FontAttributeKey](./fontattributekey/fontname.md)
  A required key for a font name.
- [static let fontSize: NSAccessibility.FontAttributeKey](./fontattributekey/fontsize.md)
  A required key for a font size.
- [static let visibleName: NSAccessibility.FontAttributeKey](./fontattributekey/visiblename.md)
  An optional key for font visibility.
### Initializers
- [init(rawValue: String)](./fontattributekey/init%28rawvalue%29.md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessibility Types
- [NSAccessibility.Action](./action.md)
  Constants that describe types of actions.
- [NSAccessibility.AnnotationAttributeKey](./annotationattributekey.md)
  Keys for annotation attributes.
- [enum NSAccessibilityAnnotationPosition](../nsaccessibilityannotationposition.md)
  Constants that specify the position where the annotation applies.
- [NSAccessibility.Attribute](./attribute.md)
  Constants that describe attributes.
- [enum NSAccessibilityOrientation](../nsaccessibilityorientation.md)
  Values that indicate the orientation of accessibility elements, such as scroll bars and split views.
- [NSAccessibility.OrientationValue](./orientationvalue.md)
  Values that indicate the orientation of user interface elements, such as scroll bars and split views.
- [NSAccessibility.ParameterizedAttribute](./parameterizedattribute.md)
  Values that describe parameterized attributes.
- [NSAccessibility.Role](./role.md)
  Values that describe types of objects that accessibility elements represent.
- [enum NSAccessibilityRulerMarkerType](../nsaccessibilityrulermarkertype.md)
  Values that indicate the marker type of an accessibility element.
- [NSAccessibility.RulerMarkerTypeValue](./rulermarkertypevalue.md)
  Values that describe ruler marker types.
- [NSAccessibility.RulerUnitValue](./rulerunitvalue.md)
  Values that indicate the unit values of a ruler or layout area.
- [NSAccessibility.SortDirectionValue](./sortdirectionvalue.md)
  Values that indicate the sort direction of a column.
- [enum NSAccessibilitySortDirection](../nsaccessibilitysortdirection.md)
  Values that indicate the sort direction of a column.
- [NSAccessibility.Subrole](./subrole.md)
  Values that describe specialized object subtypes that accessibility elements represent.
- [enum NSAccessibilityUnits](../nsaccessibilityunits.md)
  Values that indicate the unit values of a ruler or layout area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/fontattributekey)*