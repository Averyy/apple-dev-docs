# NSAccessibility.AnnotationAttributeKey

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Keys for annotation attributes.

**Availability**:
- macOS

## Declaration

```swift
struct AnnotationAttributeKey
```

```c
typedef NSString * NSAccessibilityAnnotationAttributeKey;
```

## Topics

### Keys
- [static let label: NSAccessibility.AnnotationAttributeKey](./annotationattributekey/label.md)
  A description of the annotation.
- [static let element: NSAccessibility.AnnotationAttributeKey](./annotationattributekey/element.md)
  The user interface element for the annotation.
- [static let location: NSAccessibility.AnnotationAttributeKey](./annotationattributekey/location.md)
  The position where the annotation applies.
### Initializer
- [init(rawValue: String)](./annotationattributekey/init%28rawvalue%29.md)
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
- [enum NSAccessibilityAnnotationPosition](../nsaccessibilityannotationposition.md)
  Constants that specify the position where the annotation applies.
- [NSAccessibility.Attribute](./attribute.md)
  Constants that describe attributes.
- [NSAccessibility.FontAttributeKey](./fontattributekey.md)
  Keys for font attributes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/annotationattributekey)*