# NSAccessibility.Attribute

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants that describe attributes.

**Availability**:
- macOS

## Declaration

```swift
struct Attribute
```

```c
typedef NSString * NSAccessibilityAttributeName;
```

## Topics

### Attributes
- [static let activationPoint: NSAccessibility.Attribute](./attribute/activationpoint.md)
- [static let allowedValues: NSAccessibility.Attribute](./attribute/allowedvalues.md)
  The allowed values in the slider (`NSArray`).
- [static let alternateUIVisible: NSAccessibility.Attribute](./attribute/alternateuivisible.md)
- [static let autoInteractableAttribute: NSAccessibility.Attribute](./attribute/autointeractableattribute.md)
- [static let blockQuoteLevelAttribute: NSAccessibility.Attribute](./attribute/blockquotelevelattribute.md)
- [static let cancelButton: NSAccessibility.Attribute](./attribute/cancelbutton.md)
  The element that represents the cancel button (`id`).
- [static let children: NSAccessibility.Attribute](./attribute/children.md)
  The element’s child elements in the accessibility hierarchy (`NSArray`).
- [static let childrenInNavigationOrderAttribute: NSAccessibility.Attribute](./attribute/childreninnavigationorderattribute.md)
- [static let clearButton: NSAccessibility.Attribute](./attribute/clearbutton.md)
  The element that represents the clear button in a search field (`id`).
- [static let closeButton: NSAccessibility.Attribute](./attribute/closebutton.md)
  The element representing the close button (`id`).
- [static let columnCount: NSAccessibility.Attribute](./attribute/columncount.md)
  The number of columns in the grid (`NSNumber` as `intValue`).
- [static let columnHeaderUIElements: NSAccessibility.Attribute](./attribute/columnheaderuielements.md)
  The table’s column headers (`NSArray`).
- [static let columnIndexRange: NSAccessibility.Attribute](./attribute/columnindexrange.md)
  The column index range of the cell (an `NSValue` instance that contains the row’s starting index and index span in the table).
- [static let columnTitles: NSAccessibility.Attribute](./attribute/columntitles.md)
  The elements that represent the column titles (`NSArray`).
- [static let columns: NSAccessibility.Attribute](./attribute/columns.md)
  The table’s columns (`NSArray`).
- [static let containsProtectedContent: NSAccessibility.Attribute](./attribute/containsprotectedcontent.md)
  A flag that indicates whether the object contains protected content.
- [static let contents: NSAccessibility.Attribute](./attribute/contents.md)
  Elements that represent the contents in the current element, such as the document view of a scroll view (`NSArray`).
- [static let criticalValue: NSAccessibility.Attribute](./attribute/criticalvalue.md)
  The critical value in a level indicator (typically, `NSNumber`).
- [static let dateTimeComponentsAttribute: NSAccessibility.Attribute](./attribute/datetimecomponentsattribute.md)
- [static let decrementButton: NSAccessibility.Attribute](./attribute/decrementbutton.md)
  The element that represents a stepper’s decrement button (`id`).
- [static let defaultButton: NSAccessibility.Attribute](./attribute/defaultbutton.md)
  The element that represents the default button (`id`).
- [static let description: NSAccessibility.Attribute](./attribute/description.md)
  The purpose of the element, not including the role (`NSString`).
- [static let disclosedByRow: NSAccessibility.Attribute](./attribute/disclosedbyrow.md)
  The row disclosing this row (`id`).
- [static let disclosedRows: NSAccessibility.Attribute](./attribute/disclosedrows.md)
  The rows disclosed by this row (`NSArray`).
- [static let disclosing: NSAccessibility.Attribute](./attribute/disclosing.md)
  A flag that indicates whether a row is disclosing other rows (`NSNumber`).
- [static let disclosureLevel: NSAccessibility.Attribute](./attribute/disclosurelevel.md)
  The indentation level of this row (`NSNumber`).
- [static let document: NSAccessibility.Attribute](./attribute/document.md)
  The URL for the file represented by the element (`NSString`).
- [static let edited: NSAccessibility.Attribute](./attribute/edited.md)
  A flag that indicates whether the element has been modified (`NSNumber`).
- [static let embeddedImageDescriptionAttribute: NSAccessibility.Attribute](./attribute/embeddedimagedescriptionattribute.md)
- [static let enabled: NSAccessibility.Attribute](./attribute/enabled.md)
  A flag that indicates the enabled state of the element (`NSNumber`).
- [static let expanded: NSAccessibility.Attribute](./attribute/expanded.md)
  A flag that indicates whether the element is expanded (`NSNumber`).
- [static let extrasMenuBar: NSAccessibility.Attribute](./attribute/extrasmenubar.md)
  The app extras menu bar (`id`).
- [static let filename: NSAccessibility.Attribute](./attribute/filename.md)
  The filename associated with the element (`NSString`).
- [static let focused: NSAccessibility.Attribute](./attribute/focused.md)
  A flag that indicates the presence of keyboard focus (`NSNumber`).
- [static let focusedUIElement: NSAccessibility.Attribute](./attribute/focuseduielement.md)
  The element with the current focus (`id`).
- [static let focusedWindow: NSAccessibility.Attribute](./attribute/focusedwindow.md)
  The app’s window that has current focus (`id`).
- [static let frontmost: NSAccessibility.Attribute](./attribute/frontmost.md)
  A flag that indicates whether the app is frontmost (`NSNumber`).
- [static let fullScreenButton: NSAccessibility.Attribute](./attribute/fullscreenbutton.md)
  The element that represents the full-screen button (`id`).
- [static let growArea: NSAccessibility.Attribute](./attribute/growarea.md)
  The element representing the grow area (`id`).
- [static let handles: NSAccessibility.Attribute](./attribute/handles.md)
  The drag handles of the item (`NSArray`).
- [static let header: NSAccessibility.Attribute](./attribute/header.md)
  The element that represents a table view’s header (`id`).
- [static let headingLevelAttribute: NSAccessibility.Attribute](./attribute/headinglevelattribute.md)
- [static let help: NSAccessibility.Attribute](./attribute/help.md)
  The help text for the element (`NSString`).
- [static let hidden: NSAccessibility.Attribute](./attribute/hidden.md)
  A flag that indicates whether the app is hidden (`NSNumber`).
- [static let horizontalScrollBar: NSAccessibility.Attribute](./attribute/horizontalscrollbar.md)
  The element that represents a scroll view’s horizontal scroll bar (`id`).
- [static let horizontalUnitDescription: NSAccessibility.Attribute](./attribute/horizontalunitdescription.md)
  The description of the layout view’s horizontal units (`NSString`).
- [static let horizontalUnits: NSAccessibility.Attribute](./attribute/horizontalunits.md)
  The units that the layout view uses for horizontal values (`NSString`).
- [static let identifier: NSAccessibility.Attribute](./attribute/identifier.md)
  The identity of the element (`NSString`).
- [static let incrementButton: NSAccessibility.Attribute](./attribute/incrementbutton.md)
  The element that represents a stepper’s increment button (`id`).
- [static let index: NSAccessibility.Attribute](./attribute/index.md)
  The index of the row or column represented by the element (`NSValue`).
- [static let insertionPointLineNumber: NSAccessibility.Attribute](./attribute/insertionpointlinenumber.md)
  The line number containing the insertion point (`NSNumber`).
- [static let labelUIElements: NSAccessibility.Attribute](./attribute/labeluielements.md)
  The elements that represent the slider’s labels (`NSArray`).
- [static let labelValue: NSAccessibility.Attribute](./attribute/labelvalue.md)
  The value of the label represented by this element (`NSNumber`).
- [static let languageAttribute: NSAccessibility.Attribute](./attribute/languageattribute.md)
- [static let linkedUIElements: NSAccessibility.Attribute](./attribute/linkeduielements.md)
  The elements with which this element is related (`NSArray`).
- [static let main: NSAccessibility.Attribute](./attribute/main.md)
  A flag that indicates whether the window is the main window (`NSNumber`).
- [static let mainWindow: NSAccessibility.Attribute](./attribute/mainwindow.md)
  The app’s main window (`id`).
- [static let markerGroupUIElement: NSAccessibility.Attribute](./attribute/markergroupuielement.md)
  A marker group user interface element (`id`).
- [static let markerType: NSAccessibility.Attribute](./attribute/markertype.md)
  The type of the marker (`NSString`).
- [static let markerTypeDescription: NSAccessibility.Attribute](./attribute/markertypedescription.md)
  The description of the marker type (`NSString`).
- [static let markerUIElements: NSAccessibility.Attribute](./attribute/markeruielements.md)
  An array of marker user interface elements (`NSArray`)
- [static let markerValues: NSAccessibility.Attribute](./attribute/markervalues.md)
  The marker values (`NSArray` of `NSNumber`).
- [static let maxValue: NSAccessibility.Attribute](./attribute/maxvalue.md)
  The element’s maximum value (`id`).
- [static let menuBar: NSAccessibility.Attribute](./attribute/menubar.md)
  The app’s menu bar (`id`).
- [static let minValue: NSAccessibility.Attribute](./attribute/minvalue.md)
  The element’s minimum value (`id`).
- [static let minimizeButton: NSAccessibility.Attribute](./attribute/minimizebutton.md)
  The element that represents the minimize button (`id`).
- [static let minimized: NSAccessibility.Attribute](./attribute/minimized.md)
  A flag that indicates whether the window is minimized (`NSNumber`).
- [static let modal: NSAccessibility.Attribute](./attribute/modal.md)
  A flag that indicates whether the window represented by this element is modal (`NSNumber`).
- [static let nextContents: NSAccessibility.Attribute](./attribute/nextcontents.md)
  The elements representing the contents that follow the current divider element, such as a subview adjacent to a split view’s splitter element (`NSArray`).
- [static let numberOfCharacters: NSAccessibility.Attribute](./attribute/numberofcharacters.md)
  The number of characters in the text (`NSNumber`).
- [static let orderedByRow: NSAccessibility.Attribute](./attribute/orderedbyrow.md)
  A flag that indicates whether the grid is in row major or column major order.
- [static let orientation: NSAccessibility.Attribute](./attribute/orientation.md)
  The element’s orientation.
- [static let overflowButton: NSAccessibility.Attribute](./attribute/overflowbutton.md)
  The element that represents a toolbar’s overflow button (`id`).
- [static let parent: NSAccessibility.Attribute](./attribute/parent.md)
  The element’s parent element in the accessibility hierarchy (`id`).
- [static let pathAttribute: NSAccessibility.Attribute](./attribute/pathattribute.md)
- [static let placeholderValue: NSAccessibility.Attribute](./attribute/placeholdervalue.md)
  The placeholder value for a control, such as a text field (`NSString`).
- [static let position: NSAccessibility.Attribute](./attribute/position.md)
  The position in points of the element’s lower-left corner in screen-relative coordinates (`NSValue`).
- [static let previousContents: NSAccessibility.Attribute](./attribute/previouscontents.md)
  The elements representing the contents that precede the current divider element, such as a subview adjacent to a split view’s splitter bar element (`NSArray`).
- [static let proxy: NSAccessibility.Attribute](./attribute/proxy.md)
  The element that represents the window’s proxy icon (`id`).
- [static let required: NSAccessibility.Attribute](./attribute/required.md)
- [static let role: NSAccessibility.Attribute](./attribute/role.md)
  The element’s type, such as `NSAccessibilityRadioButtonRole` (`NSString`). See Roles for a list of available roles.
- [static let roleDescription: NSAccessibility.Attribute](./attribute/roledescription.md)
  A localized, human-intelligible description of the element’s role, such as `radio button` (`NSString`).
- [static let rowCount: NSAccessibility.Attribute](./attribute/rowcount.md)
  The number of rows in the grid (`NSNumber` as `intValue`).
- [static let rowHeaderUIElements: NSAccessibility.Attribute](./attribute/rowheaderuielements.md)
  The table’s row headers (`NSArray`).
- [static let rowIndexRange: NSAccessibility.Attribute](./attribute/rowindexrange.md)
  The row index range of the cell (an `NSValue` instance that contains the row’s starting index and index span in the table).
- [static let rows: NSAccessibility.Attribute](./attribute/rows.md)
  The table’s rows (`NSArray`).
- [static let searchButton: NSAccessibility.Attribute](./attribute/searchbutton.md)
  The element that represents the search button in a search field (`id`).
- [static let searchMenu: NSAccessibility.Attribute](./attribute/searchmenu.md)
  The element that represents the menu in a search field (`id`).
- [static let selected: NSAccessibility.Attribute](./attribute/selected.md)
  A flag that indicates whether the element is selected (`NSNumber`).
- [static let selectedCells: NSAccessibility.Attribute](./attribute/selectedcells.md)
  The table’s selected cells (`NSArray`). This attribute is required for cell-based tables.
- [static let selectedChildren: NSAccessibility.Attribute](./attribute/selectedchildren.md)
  The currently selected children of the element (`NSArray`).
- [static let selectedColumns: NSAccessibility.Attribute](./attribute/selectedcolumns.md)
  The table’s selected columns (`NSArray`).
- [static let selectedRows: NSAccessibility.Attribute](./attribute/selectedrows.md)
  The table’s selected rows (`NSArray`).
- [static let selectedText: NSAccessibility.Attribute](./attribute/selectedtext.md)
  The currently selected text (`NSString`).
- [static let selectedTextRange: NSAccessibility.Attribute](./attribute/selectedtextrange.md)
  The range of selected text (`NSValue`).
- [static let selectedTextRanges: NSAccessibility.Attribute](./attribute/selectedtextranges.md)
  An array of `NSValue` (`rangeValue`) ranges of selected text (`NSArray`).
- [static let servesAsTitleForUIElements: NSAccessibility.Attribute](./attribute/servesastitleforuielements.md)
  The elements for which this element serves as the title (`NSArray`).
- [static let sharedCharacterRange: NSAccessibility.Attribute](./attribute/sharedcharacterrange.md)
  The (`rangeValue`) part of shared text in this view (`NSValue`).
- [static let sharedFocusElements: NSAccessibility.Attribute](./attribute/sharedfocuselements.md)
- [static let sharedTextUIElements: NSAccessibility.Attribute](./attribute/sharedtextuielements.md)
  The elements with which the text of this element is shared (`NSArray`).
- [static let shownMenu: NSAccessibility.Attribute](./attribute/shownmenu.md)
  The menu currently being displayed (`id`).
- [static let size: NSAccessibility.Attribute](./attribute/size.md)
  The element’s size in points (`NSValue`).
- [static let sortDirection: NSAccessibility.Attribute](./attribute/sortdirection.md)
  The column’s sort direction (`NSString`).
- [static let splitters: NSAccessibility.Attribute](./attribute/splitters.md)
  The views and splitter bar in a split view (`NSArray`).
- [static let subrole: NSAccessibility.Attribute](./attribute/subrole.md)
  The element’s subrole, such as `NSAccessibilityTableRowSubrole` (`NSString`). See Subroles for a list of available subroles.
- [static let tabs: NSAccessibility.Attribute](./attribute/tabs.md)
  The tab elements in a tab view (`NSArray`).
- [static let textInputMarkedRangeAttribute: NSAccessibility.Attribute](./attribute/textinputmarkedrangeattribute.md)
- [static let title: NSAccessibility.Attribute](./attribute/title.md)
  The title of the element, such as a button’s visible text (`NSString`).
- [static let titleUIElement: NSAccessibility.Attribute](./attribute/titleuielement.md)
  An element that represents another element’s static text title (`id`).
- [static let toolbarButton: NSAccessibility.Attribute](./attribute/toolbarbutton.md)
  The element that represents the toolbar button (`id`).
- [static let topLevelUIElement: NSAccessibility.Attribute](./attribute/topleveluielement.md)
  The top-level element that contains this element (`id`).
- [static let unitDescription: NSAccessibility.Attribute](./attribute/unitdescription.md)
  The description of ruler units (`NSString`).
- [static let units: NSAccessibility.Attribute](./attribute/units.md)
  The ruler units (`NSString`).
- [static let url: NSAccessibility.Attribute](./attribute/url.md)
  The URL associated with the element (`NSURL`).
- [static let value: NSAccessibility.Attribute](./attribute/value.md)
  The element’s value (`id`).
- [static let valueDescription: NSAccessibility.Attribute](./attribute/valuedescription.md)
  The description of the element’s value (`NSString`).
- [static let verticalScrollBar: NSAccessibility.Attribute](./attribute/verticalscrollbar.md)
  The element that represents the vertical scroll bar in a scroll view (`id`).
- [static let verticalUnitDescription: NSAccessibility.Attribute](./attribute/verticalunitdescription.md)
  The description of the layout view’s vertical units (`NSString`).
- [static let verticalUnits: NSAccessibility.Attribute](./attribute/verticalunits.md)
  The units that the layout view uses for vertical values (`NSString`).
- [static let visibleCells: NSAccessibility.Attribute](./attribute/visiblecells.md)
  The table’s visible cells (`NSArray`). This attribute is required for cell-based tables.
- [static let visibleCharacterRange: NSAccessibility.Attribute](./attribute/visiblecharacterrange.md)
  The range of visible text (`NSValue`).
- [static let visibleChildren: NSAccessibility.Attribute](./attribute/visiblechildren.md)
  The element’s child elements that are visible (`NSArray`).
- [static let visibleColumns: NSAccessibility.Attribute](./attribute/visiblecolumns.md)
  The table’s visible columns (`NSArray`).
- [static let visibleRows: NSAccessibility.Attribute](./attribute/visiblerows.md)
  The table’s visible rows (`NSArray`).
- [static let visitedAttribute: NSAccessibility.Attribute](./attribute/visitedattribute.md)
- [static let warningValue: NSAccessibility.Attribute](./attribute/warningvalue.md)
  The warning value in a level indicator (typically, `NSNumber`).
- [static let window: NSAccessibility.Attribute](./attribute/window.md)
  The window containing the current element (`id`).
- [static let windows: NSAccessibility.Attribute](./attribute/windows.md)
  The app’s windows (`NSArray`).
- [static let zoomButton: NSAccessibility.Attribute](./attribute/zoombutton.md)
  The element that represents the zoom button (`id`).
- [static let matteContentUIElement: NSAccessibility.Attribute](./attribute/mattecontentuielement.md)
  The element that is clipped by the matte (`id`).
- [static let matteHole: NSAccessibility.Attribute](./attribute/mattehole.md)
  The bounds of the matte hole, in screen coordinates in points (`NSValue` containing an `NSRect`).
### Initializers
- [init(rawValue: String)](./attribute/init%28rawvalue%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/attribute)*