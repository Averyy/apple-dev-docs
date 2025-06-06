# NSAccessibility.Attribute

**Framework**: AppKit  
**Kind**: struct

Constants that describe attributes.

**Availability**:
- macOS ?+

## Declaration

```swift
struct Attribute
```

## Topics

### Attributes
- [static let activationPoint: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/activationpoint.md)
- [static let allowedValues: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/allowedvalues.md)
  The allowed values in the slider (`NSArray`).
- [static let alternateUIVisible: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/alternateuivisible.md)
- [static let cancelButton: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/cancelbutton.md)
  The element that represents the cancel button (`id`).
- [static let children: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/children.md)
  The element’s child elements in the accessibility hierarchy (`NSArray`).
- [static let clearButton: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/clearbutton.md)
  The element that represents the clear button in a search field (`id`).
- [static let closeButton: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/closebutton.md)
  The element representing the close button (`id`).
- [static let columnCount: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/columncount.md)
  The number of columns in the grid (`NSNumber` as `intValue`).
- [static let columnHeaderUIElements: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/columnheaderuielements.md)
  The table’s column headers (`NSArray`).
- [static let columnIndexRange: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/columnindexrange.md)
  The column index range of the cell (an `NSValue` instance that contains the row’s starting index and index span in the table).
- [static let columnTitles: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/columntitles.md)
  The elements that represent the column titles (`NSArray`).
- [static let columns: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/columns.md)
  The table’s columns (`NSArray`).
- [static let containsProtectedContent: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/containsprotectedcontent.md)
  A flag that indicates whether the object contains protected content ([`true`](https://developer.apple.com/documentation/swift/true)), or not ([`false`](https://developer.apple.com/documentation/swift/false)) (`NSNumber` as `boolValue`).
- [static let contents: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/contents.md)
  Elements that represent the contents in the current element, such as the document view of a scroll view (`NSArray`).
- [static let criticalValue: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/criticalvalue.md)
  The critical value in a level indicator (typically, `NSNumber`).
- [static let decrementButton: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/decrementbutton.md)
  The element that represents a stepper’s decrement button (`id`).
- [static let defaultButton: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/defaultbutton.md)
  The element that represents the default button (`id`).
- [static let description: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/description.md)
  The purpose of the element, not including the role (`NSString`).
- [static let disclosedByRow: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/disclosedbyrow.md)
  The row disclosing this row (`id`).
- [static let disclosedRows: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/disclosedrows.md)
  The rows disclosed by this row (`NSArray`).
- [static let disclosing: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/disclosing.md)
  A flag that indicates whether a row is disclosing other rows (`NSNumber`).
- [static let disclosureLevel: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/disclosurelevel.md)
  The indentation level of this row (`NSNumber`).
- [static let document: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/document.md)
  The URL for the file represented by the element (`NSString`).
- [static let edited: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/edited.md)
  A flag that indicates whether the element has been modified (`NSNumber`).
- [static let enabled: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/enabled.md)
  A flag that indicates the enabled state of the element (`NSNumber`).
- [static let expanded: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/expanded.md)
  A flag that indicates whether the element is expanded (`NSNumber`).
- [static let extrasMenuBar: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/extrasmenubar.md)
  The app extras menu bar (`id`).
- [static let filename: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/filename.md)
  The filename associated with the element (`NSString`).
- [static let focused: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/focused.md)
  A flag that indicates the presence of keyboard focus (`NSNumber`).
- [static let focusedUIElement: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/focuseduielement.md)
  The element with the current focus (`id`).
- [static let focusedWindow: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/focusedwindow.md)
  The app’s window that has current focus (`id`).
- [static let frontmost: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/frontmost.md)
  A flag that indicates whether the app is frontmost (`NSNumber`).
- [static let fullScreenButton: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/fullscreenbutton.md)
  The element that represents the full-screen button (`id`).
- [static let growArea: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/growarea.md)
  The element representing the grow area (`id`).
- [static let handles: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/handles.md)
  The drag handles of the item (`NSArray`).
- [static let header: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/header.md)
  The element that represents a table view’s header (`id`).
- [static let help: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/help.md)
  The help text for the element (`NSString`).
- [static let hidden: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/hidden.md)
  A flag that indicates whether the app is hidden (`NSNumber`).
- [static let horizontalScrollBar: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/horizontalscrollbar.md)
  The element that represents a scroll view’s horizontal scroll bar (`id`).
- [static let horizontalUnitDescription: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/horizontalunitdescription.md)
  The description of the layout view’s horizontal units (`NSString`).
- [static let horizontalUnits: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/horizontalunits.md)
  The units that the layout view uses for horizontal values (`NSString`). See Measurement unit attributes for possible values.
- [static let identifier: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/identifier.md)
  The identity of the element (`NSString`).
- [static let incrementButton: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/incrementbutton.md)
  The element that represents a stepper’s increment button (`id`).
- [static let index: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/index.md)
  The index of the row or column represented by the element (`NSValue`).
- [static let insertionPointLineNumber: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/insertionpointlinenumber.md)
  The line number containing the insertion point (`NSNumber`).
- [static let labelUIElements: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/labeluielements.md)
  The elements that represent the slider’s labels (`NSArray`).
- [static let labelValue: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/labelvalue.md)
  The value of the label represented by this element (`NSNumber`).
- [static let linkedUIElements: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/linkeduielements.md)
  The elements with which this element is related (`NSArray`).
- [static let main: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/main.md)
  A flag that indicates whether the window is the main window (`NSNumber`).
- [static let mainWindow: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/mainwindow.md)
  The app’s main window (`id`).
- [static let markerGroupUIElement: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/markergroupuielement.md)
  A marker group user interface element (`id`).
- [static let markerType: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/markertype.md)
  The type of the marker (`NSString`). See Ruler Marker Type Values for possible values.
- [static let markerTypeDescription: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/markertypedescription.md)
  The description of the marker type (`NSString`).
- [static let markerUIElements: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/markeruielements.md)
  An array of marker user interface elements (`NSArray`)
- [static let markerValues: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/markervalues.md)
  The marker values (`NSArray` of `NSNumber`).
- [static let matteContentUIElement: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/mattecontentuielement.md)
  The element that is clipped by the matte (`id`).
- [static let matteHole: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/mattehole.md)
  The bounds of the matte hole, in screen coordinates in points (`NSValue` containing an `NSRect`).
- [static let maxValue: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/maxvalue.md)
  The element’s maximum value (`id`).
- [static let menuBar: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/menubar.md)
  The app’s menu bar (`id`).
- [static let minValue: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/minvalue.md)
  The element’s minimum value (`id`).
- [static let minimizeButton: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/minimizebutton.md)
  The element that represents the minimize button (`id`).
- [static let minimized: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/minimized.md)
  A flag that indicates whether the window is minimized (`NSNumber`).
- [static let modal: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/modal.md)
  A flag that indicates whether the window represented by this element is modal (`NSNumber`).
- [static let nextContents: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/nextcontents.md)
  The elements representing the contents that follow the current divider element, such as a subview adjacent to a split view’s splitter element (`NSArray`).
- [static let numberOfCharacters: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/numberofcharacters.md)
  The number of characters in the text (`NSNumber`).
- [static let orderedByRow: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/orderedbyrow.md)
  A flag that indicates whether the grid is ordered row major ([`true`](https://developer.apple.com/documentation/swift/true)), or column major ([`false`](https://developer.apple.com/documentation/swift/false)) (`NSNumber` as `boolValue`).
- [static let orientation: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/orientation.md)
  The element’s orientation, which can have the value [`horizontal`](nsaccessibility-swift.struct/orientationvalue/horizontal.md) or  [`vertical`](nsaccessibility-swift.struct/orientationvalue/vertical.md).
- [static let overflowButton: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/overflowbutton.md)
  The element that represents a toolbar’s overflow button (`id`).
- [static let parent: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/parent.md)
  The element’s parent element in the accessibility hierarchy (`id`).
- [static let placeholderValue: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/placeholdervalue.md)
  The placeholder value for a control, such as a text field (`NSString`).
- [static let position: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/position.md)
  The position in points of the element’s lower-left corner in screen-relative coordinates (`NSValue`).
- [static let previousContents: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/previouscontents.md)
  The elements representing the contents that precede the current divider element, such as a subview adjacent to a split view’s splitter bar element (`NSArray`).
- [static let proxy: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/proxy.md)
  The element that represents the window’s proxy icon (`id`).
- [static let required: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/required.md)
- [static let role: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/role.md)
  The element’s type, such as `NSAccessibilityRadioButtonRole` (`NSString`). See Roles for a list of available roles.
- [static let roleDescription: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/roledescription.md)
  A localized, human-intelligible description of the element’s role, such as `radio button` (`NSString`).
- [static let rowCount: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/rowcount.md)
  The number of rows in the grid (`NSNumber` as `intValue`).
- [static let rowHeaderUIElements: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/rowheaderuielements.md)
  The table’s row headers (`NSArray`).
- [static let rowIndexRange: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/rowindexrange.md)
  The row index range of the cell (an `NSValue` instance that contains the row’s starting index and index span in the table).
- [static let rows: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/rows.md)
  The table’s rows (`NSArray`).
- [static let searchButton: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/searchbutton.md)
  The element that represents the search button in a search field (`id`).
- [static let searchMenu: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/searchmenu.md)
  The element that represents the menu in a search field (`id`).
- [static let selected: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/selected.md)
  A flag that indicates whether the element is selected (`NSNumber`).
- [static let selectedCells: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/selectedcells.md)
  The table’s selected cells (`NSArray`). This attribute is required for cell-based tables.
- [static let selectedChildren: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/selectedchildren.md)
  The currently selected children of the element (`NSArray`).
- [static let selectedColumns: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/selectedcolumns.md)
  The table’s selected columns (`NSArray`).
- [static let selectedRows: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/selectedrows.md)
  The table’s selected rows (`NSArray`).
- [static let selectedText: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/selectedtext.md)
  The currently selected text (`NSString`).
- [static let selectedTextRange: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/selectedtextrange.md)
  The range of selected text (`NSValue`).
- [static let selectedTextRanges: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/selectedtextranges.md)
  An array of `NSValue` (`rangeValue`) ranges of selected text (`NSArray`).
- [static let servesAsTitleForUIElements: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/servesastitleforuielements.md)
  The elements for which this element serves as the title (`NSArray`).
- [static let sharedCharacterRange: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/sharedcharacterrange.md)
  The (`rangeValue`) part of shared text in this view (`NSValue`).
- [static let sharedFocusElements: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/sharedfocuselements.md)
- [static let sharedTextUIElements: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/sharedtextuielements.md)
  The elements with which the text of this element is shared (`NSArray`).
- [static let shownMenu: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/shownmenu.md)
  The menu currently being displayed (`id`).
- [static let size: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/size.md)
  The element’s size in points (`NSValue`).
- [static let sortDirection: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/sortdirection.md)
  The column’s sort direction (`NSString`). See Column Sort Direction  for possible values.
- [static let splitters: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/splitters.md)
  The views and splitter bar in a split view (`NSArray`).
- [static let subrole: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/subrole.md)
  The element’s subrole, such as `NSAccessibilityTableRowSubrole` (`NSString`). See Subroles for a list of available subroles.
- [static let tabs: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/tabs.md)
  The tab elements in a tab view (`NSArray`).
- [static let title: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/title.md)
  The title of the element, such as a button’s visible text (`NSString`).
- [static let titleUIElement: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/titleuielement.md)
  An element that represents another element’s static text title (`id`).
- [static let toolbarButton: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/toolbarbutton.md)
  The element that represents the toolbar button (`id`).
- [static let topLevelUIElement: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/topleveluielement.md)
  The top-level element that contains this element (`id`).
- [static let unitDescription: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/unitdescription.md)
  The description of ruler units (`NSString`).
- [static let units: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/units.md)
  The ruler units (`NSString`). See Measurement Unit Attributes for possible values.
- [static let url: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/url.md)
  The URL associated with the element (`NSURL`).
- [static let value: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/value.md)
  The element’s value (`id`).
- [static let valueDescription: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/valuedescription.md)
  The description of the element’s value (`NSString`).
- [static let verticalScrollBar: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/verticalscrollbar.md)
  The element that represents the vertical scroll bar in a scroll view (`id`).
- [static let verticalUnitDescription: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/verticalunitdescription.md)
  The description of the layout view’s vertical units (`NSString`).
- [static let verticalUnits: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/verticalunits.md)
  The units that the layout view uses for vertical values (`NSString`). See Measurement unit attributes for possible values.
- [static let visibleCells: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/visiblecells.md)
  The table’s visible cells (`NSArray`). This attribute is required for cell-based tables.
- [static let visibleCharacterRange: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/visiblecharacterrange.md)
  The range of visible text (`NSValue`).
- [static let visibleChildren: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/visiblechildren.md)
  The element’s child elements that are visible (`NSArray`).
- [static let visibleColumns: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/visiblecolumns.md)
  The table’s visible columns (`NSArray`).
- [static let visibleRows: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/visiblerows.md)
  The table’s visible rows (`NSArray`).
- [static let warningValue: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/warningvalue.md)
  The warning value in a level indicator (typically, `NSNumber`).
- [static let window: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/window.md)
  The window containing the current element (`id`).
- [static let windows: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/windows.md)
  The app’s windows (`NSArray`).
- [static let zoomButton: NSAccessibility.Attribute](nsaccessibility-swift.struct/attribute/zoombutton.md)
  The element that represents the zoom button (`id`).
### Initializers
- [init(rawValue: String)](nsaccessibility-swift.struct/attribute/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [NSAccessibility.Action](nsaccessibility-swift.struct/action.md)
  Constants that describe types of actions.
- [NSAccessibility.AnnotationAttributeKey](nsaccessibility-swift.struct/annotationattributekey.md)
  Keys for annotation attributes.
- [enum NSAccessibilityAnnotationPosition](nsaccessibilityannotationposition.md)
  Constants that specify the position where the annotation applies.
- [NSAccessibility.FontAttributeKey](nsaccessibility-swift.struct/fontattributekey.md)
  Keys for font attributes.
- [enum NSAccessibilityOrientation](nsaccessibilityorientation.md)
  Values that indicate the orientation of accessibility elements, such as scroll bars and split views.
- [NSAccessibility.OrientationValue](nsaccessibility-swift.struct/orientationvalue.md)
  Values that indicate the orientation of user interface elements, such as scroll bars and split views.
- [NSAccessibility.ParameterizedAttribute](nsaccessibility-swift.struct/parameterizedattribute.md)
  Values that describe parameterized attributes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/attribute)*