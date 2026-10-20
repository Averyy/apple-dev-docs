# NSAccessibility.Subrole

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Values that describe specialized object subtypes that accessibility elements represent.

**Availability**:
- macOS

## Declaration

```swift
struct Subrole
```

```c
typedef NSString * NSAccessibilitySubrole;
```

## Topics

### Subroles
- [static let closeButton: NSAccessibility.Subrole](./subrole/closebutton.md)
  A window’s close button subrole.
- [static let collectionListSubrole: NSAccessibility.Subrole](./subrole/collectionlistsubrole.md)
- [static let contentList: NSAccessibility.Subrole](./subrole/contentlist.md)
  A subrole for content that is organized in a list, but is not in a list control or table view.
- [static let decrementArrow: NSAccessibility.Subrole](./subrole/decrementarrow.md)
  A decrement arrow subrole (the down arrow in a scroll bar).
- [static let decrementPage: NSAccessibility.Subrole](./subrole/decrementpage.md)
  A decrement page subrole (the decrement area in the scroll track of a scroll bar).
- [static let definitionList: NSAccessibility.Subrole](./subrole/definitionlist.md)
  A subrole for a content list in a webpage.
- [static let descriptionList: NSAccessibility.Subrole](./subrole/descriptionlist.md)
  A description list subrole.
- [static let dialog: NSAccessibility.Subrole](./subrole/dialog.md)
  A dialog subrole.
- [static let floatingWindow: NSAccessibility.Subrole](./subrole/floatingwindow.md)
  A floating window subrole.
- [static let fullScreenButton: NSAccessibility.Subrole](./subrole/fullscreenbutton.md)
  A window’s full-screen button subrole.
- [static let incrementArrow: NSAccessibility.Subrole](./subrole/incrementarrow.md)
  An increment arrow subrole (the up arrow in a scroll bar).
- [static let incrementPage: NSAccessibility.Subrole](./subrole/incrementpage.md)
  An increment page subrole (the increment area in the scroll track of a scroll bar).
- [static let minimizeButton: NSAccessibility.Subrole](./subrole/minimizebutton.md)
  A window’s minimize button subrole.
- [static let outlineRow: NSAccessibility.Subrole](./subrole/outlinerow.md)
  An outline row subrole.
- [static let ratingIndicator: NSAccessibility.Subrole](./subrole/ratingindicator.md)
  A rating indicator subrole.
- [static let searchField: NSAccessibility.Subrole](./subrole/searchfield.md)
  A search field subrole.
- [static let sectionListSubrole: NSAccessibility.Subrole](./subrole/sectionlistsubrole.md)
- [static let secureTextField: NSAccessibility.Subrole](./subrole/securetextfield.md)
  A secure text field subrole.
- [static let sortButton: NSAccessibility.Subrole](./subrole/sortbutton.md)
  A sort button subrole for a table or outline view.
- [static let standardWindow: NSAccessibility.Subrole](./subrole/standardwindow.md)
  A standard window subrole.
- [static let suggestionSubrole: NSAccessibility.Subrole](./subrole/suggestionsubrole.md)
- [static let `switch`: NSAccessibility.Subrole](./subrole/switch.md)
  A switch subrole.
- [static let systemDialog: NSAccessibility.Subrole](./subrole/systemdialog.md)
  A system dialog subrole (a system-generated dialog that floats on the top layer, regardless of which app is frontmost).
- [static let systemFloatingWindow: NSAccessibility.Subrole](./subrole/systemfloatingwindow.md)
  A system floating window subrole (a system-generated panel).
- [static let tabButtonSubrole: NSAccessibility.Subrole](./subrole/tabbuttonsubrole.md)
- [static let tableRow: NSAccessibility.Subrole](./subrole/tablerow.md)
  A table row subrole.
- [static let textAttachment: NSAccessibility.Subrole](./subrole/textattachment.md)
  A text attachment subrole.
- [static let textLink: NSAccessibility.Subrole](./subrole/textlink.md)
  A text link subrole.
- [static let timeline: NSAccessibility.Subrole](./subrole/timeline.md)
  A timeline subrole.
- [static let toggle: NSAccessibility.Subrole](./subrole/toggle.md)
  A toggle subrole.
- [static let toolbarButton: NSAccessibility.Subrole](./subrole/toolbarbutton.md)
  A window’s toolbar button subrole.
- [static let unknown: NSAccessibility.Subrole](./subrole/unknown.md)
  An unknown subrole.
- [static let zoomButton: NSAccessibility.Subrole](./subrole/zoombutton.md)
  A window’s zoom button subrole.
### Initializers
- [init(rawValue: String)](./subrole/init%28rawvalue%29.md)

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
- [enum NSAccessibilityUnits](../nsaccessibilityunits.md)
  Values that indicate the unit values of a ruler or layout area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/subrole)*