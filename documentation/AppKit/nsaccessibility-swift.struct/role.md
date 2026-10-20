# NSAccessibility.Role

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Values that describe types of objects that accessibility elements represent.

**Availability**:
- macOS

## Declaration

```swift
struct Role
```

```c
typedef NSString * NSAccessibilityRole;
```

## Topics

### Roles
- [static let application: NSAccessibility.Role](./role/application.md)
  The app role.
- [static let browser: NSAccessibility.Role](./role/browser.md)
  The browser role.
- [static let busyIndicator: NSAccessibility.Role](./role/busyindicator.md)
  The busy indicator role.
- [static let button: NSAccessibility.Role](./role/button.md)
  The button role.
- [static let cell: NSAccessibility.Role](./role/cell.md)
  The cell role in a table or matrix.
- [static let checkBox: NSAccessibility.Role](./role/checkbox.md)
  The checkbox role.
- [static let colorWell: NSAccessibility.Role](./role/colorwell.md)
  The color well role.
- [static let column: NSAccessibility.Role](./role/column.md)
  The column role.
- [static let comboBox: NSAccessibility.Role](./role/combobox.md)
  The combo box role.
- [static let dateTimeAreaRole: NSAccessibility.Role](./role/datetimearearole.md)
- [static let disclosureTriangle: NSAccessibility.Role](./role/disclosuretriangle.md)
  The disclosure triangle role.
- [static let drawer: NSAccessibility.Role](./role/drawer.md)
  The drawer role.
- [static let grid: NSAccessibility.Role](./role/grid.md)
  The grid role.
- [static let group: NSAccessibility.Role](./role/group.md)
  The group role.
- [static let growArea: NSAccessibility.Role](./role/growarea.md)
  The grow (resize) area role in a window.
- [static let handle: NSAccessibility.Role](./role/handle.md)
  The drag handle role.
- [static let headingRole: NSAccessibility.Role](./role/headingrole.md)
- [static let helpTag: NSAccessibility.Role](./role/helptag.md)
  The help tag role.
- [static let image: NSAccessibility.Role](./role/image.md)
  The image role.
- [static let incrementor: NSAccessibility.Role](./role/incrementor.md)
  The stepper role.
- [static let layoutArea: NSAccessibility.Role](./role/layoutarea.md)
  The layout area role (a view, such as a graphic view, that contains visual elements that may not have any accessibility representation).
- [static let layoutItem: NSAccessibility.Role](./role/layoutitem.md)
  The role for an item in a layout area.
- [static let levelIndicator: NSAccessibility.Role](./role/levelindicator.md)
  The level indicator role.
- [static let link: NSAccessibility.Role](./role/link.md)
  The link role.
- [static let list: NSAccessibility.Role](./role/list.md)
  The list role.
- [static let listMarkerRole: NSAccessibility.Role](./role/listmarkerrole.md)
- [static let matte: NSAccessibility.Role](./role/matte.md)
  The matte role.
- [static let menu: NSAccessibility.Role](./role/menu.md)
  The menu role.
- [static let menuBar: NSAccessibility.Role](./role/menubar.md)
  The menu bar role.
- [static let menuBarItem: NSAccessibility.Role](./role/menubaritem.md)
  The menu bar item role.
- [static let menuButton: NSAccessibility.Role](./role/menubutton.md)
  The menu button role.
- [static let menuItem: NSAccessibility.Role](./role/menuitem.md)
  The menu item role.
- [static let outline: NSAccessibility.Role](./role/outline.md)
  The outline role.
- [static let pageRole: NSAccessibility.Role](./role/pagerole.md)
  The page role.
- [static let popUpButton: NSAccessibility.Role](./role/popupbutton.md)
  The pop-up button role.
- [static let popover: NSAccessibility.Role](./role/popover.md)
  The popover role.
- [static let progressIndicator: NSAccessibility.Role](./role/progressindicator.md)
  The progress indicator role.
- [static let radioButton: NSAccessibility.Role](./role/radiobutton.md)
  The radio button role.
- [static let radioGroup: NSAccessibility.Role](./role/radiogroup.md)
  The radio button group role.
- [static let relevanceIndicator: NSAccessibility.Role](./role/relevanceindicator.md)
  The relevance indicator role.
- [static let row: NSAccessibility.Role](./role/row.md)
  The row role.
- [static let ruler: NSAccessibility.Role](./role/ruler.md)
  The ruler role.
- [static let rulerMarker: NSAccessibility.Role](./role/rulermarker.md)
  The ruler marker role.
- [static let scrollArea: NSAccessibility.Role](./role/scrollarea.md)
  The scroll view role.
- [static let scrollBar: NSAccessibility.Role](./role/scrollbar.md)
  The scroll bar role.
- [static let sheet: NSAccessibility.Role](./role/sheet.md)
  The sheet role.
- [static let slider: NSAccessibility.Role](./role/slider.md)
  The slider role.
- [static let splitGroup: NSAccessibility.Role](./role/splitgroup.md)
  The split view role.
- [static let splitter: NSAccessibility.Role](./role/splitter.md)
  The splitter bar role for a split view.
- [static let staticText: NSAccessibility.Role](./role/statictext.md)
  The uneditable text role.
- [static let systemWide: NSAccessibility.Role](./role/systemwide.md)
  The systemwide accessibility object role.
- [static let tabGroup: NSAccessibility.Role](./role/tabgroup.md)
  The tab group role.
- [static let table: NSAccessibility.Role](./role/table.md)
  The table role.
- [static let textArea: NSAccessibility.Role](./role/textarea.md)
  The text view role.
- [static let textField: NSAccessibility.Role](./role/textfield.md)
  The text field role.
- [static let toolbar: NSAccessibility.Role](./role/toolbar.md)
  The toolbar role.
- [static let valueIndicator: NSAccessibility.Role](./role/valueindicator.md)
  The value indicator role.
- [static let webAreaRole: NSAccessibility.Role](./role/webarearole.md)
- [static let window: NSAccessibility.Role](./role/window.md)
  The window role.
- [static let unknown: NSAccessibility.Role](./role/unknown.md)
  An object with an unknown role.
### Descriptions
- [func description(with: NSAccessibility.Subrole?) -> String?](./role/description%28with%29.md)
  Returns a standard description for a role and subrole.
- [static func description(for: Any) -> String?](./role/description%28for%29.md)
  Returns a standard role description for a user interface element.
### Initializers
- [init(rawValue: String)](./role/init%28rawvalue%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/role)*