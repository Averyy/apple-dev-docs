# NSRuleEditor

**Framework**: AppKit  
**Kind**: class

An interface for configuring a rule-based list of options.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSRuleEditor
```

#### Overview

A rule editor lets the user visually create and configure a list of options that are expressed as a predicate (as described in [`Predicate Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/AdditionalChapters/Introduction.html#//apple_ref/doc/uid/TP40001789)). Each row displayed by the rule editor represents a particular path down a tree of choices. The rule editor’s delegate provides the tree of choices to be displayed. The rule editor presents those choices to the user as a row of popup buttons, static text fields, and custom views.

`NSRuleEditor` exposes one binding, `rows`. You can bind `rows` to an ordered collection (such as an instance of `NSMutableArray`). Each object in the collection should have the following properties:

> **Note**: If you override [`viewDidMoveToWindow()`](nsview/viewdidmovetowindow().md) in a subclass of [`NSRuleEditor`](nsruleeditor.md), you must invoke super’s implementation.

## Topics

### Configuring the Delegate
- [var delegate: (any NSRuleEditorDelegate)?](nsruleeditor/delegate.md)
  The rule editor’s delegate.
- [protocol NSRuleEditorDelegate](nsruleeditordelegate.md)
  The `NSRuleEditorDelegate` protocol defines the optional methods implemented by delegates of [`NSRuleEditor`](nsruleeditor.md) objects.
### Configuring a Rule Editor
- [var isEditable: Bool](nsruleeditor/iseditable.md)
  A Boolean value that determines whether the rule editor is editable.
- [var nestingMode: NSRuleEditor.NestingMode](nsruleeditor/nestingmode-swift.property.md)
  The rule editor’s nesting mode.
- [NSRuleEditor.NestingMode](nsruleeditor/nestingmode-swift.enum.md)
  Specifies a type for nesting modes.
- [var canRemoveAllRows: Bool](nsruleeditor/canremoveallrows.md)
  A Boolean value that indicates whether all the rows can be removed.
- [var rowHeight: CGFloat](nsruleeditor/rowheight.md)
  The rule editor’s row height.
### Working with Formatting
- [var formattingDictionary: [String : String]?](nsruleeditor/formattingdictionary.md)
  The formatting dictionary for the rule editor.
- [var formattingStringsFilename: String?](nsruleeditor/formattingstringsfilename.md)
  The name of the rule editor’s strings file.
### Providing Data
- [func reloadCriteria()](nsruleeditor/reloadcriteria.md)
  Instructs the receiver to refetch criteria from its delegate.
- [func setCriteria([Any], andDisplayValues: [Any], forRowAt: Int)](nsruleeditor/setcriteria(_:anddisplayvalues:forrowat:).md)
  Modifies the row at a given index to contain the given items and values.
- [func criteria(forRow: Int) -> [Any]](nsruleeditor/criteria(forrow:).md)
  Returns the currently chosen items for a given row.
- [func displayValues(forRow: Int) -> [Any]](nsruleeditor/displayvalues(forrow:).md)
  Returns the chosen values for a given row.
### Obtaining Row Information
- [var numberOfRows: Int](nsruleeditor/numberofrows.md)
  The number of rows in the rule editor.
- [func parentRow(forRow: Int) -> Int](nsruleeditor/parentrow(forrow:).md)
  Returns the index of the parent of a given row.
- [func row(forDisplayValue: Any) -> Int](nsruleeditor/row(fordisplayvalue:).md)
  Returns the index of the row containing a given value.
- [func rowType(forRow: Int) -> NSRuleEditor.RowType](nsruleeditor/rowtype(forrow:).md)
  Returns the type of a given row.
- [NSRuleEditor.RowType](nsruleeditor/rowtype.md)
  Specifies a type for row types.
- [func subrowIndexes(forRow: Int) -> IndexSet](nsruleeditor/subrowindexes(forrow:).md)
  Returns the immediate subrows of a given row.
### Working with the Selection
- [var selectedRowIndexes: IndexSet](nsruleeditor/selectedrowindexes.md)
  The indexes of the rule editor’s selected rows.
- [func selectRowIndexes(IndexSet, byExtendingSelection: Bool)](nsruleeditor/selectrowindexes(_:byextendingselection:).md)
  Sets in the receiver the indexes of rows that are selected.
### Manipulating Rows
- [func addRow(Any?)](nsruleeditor/addrow(_:).md)
  Adds a row to the receiver.
- [func insertRow(at: Int, with: NSRuleEditor.RowType, asSubrowOfRow: Int, animate: Bool)](nsruleeditor/insertrow(at:with:assubrowofrow:animate:).md)
  Adds a new row of a given type at a given location.
- [func removeRow(at: Int)](nsruleeditor/removerow(at:).md)
  Removes the row at a given index.
- [func removeRows(at: IndexSet, includeSubrows: Bool)](nsruleeditor/removerows(at:includesubrows:).md)
  Removes the rows at given indexes.
### Working with Predicates
- [var predicate: NSPredicate?](nsruleeditor/predicate.md)
  The rule editor’s predicate.
- [func reloadPredicate()](nsruleeditor/reloadpredicate.md)
  Instructs the receiver to regenerate its predicate by invoking the corresponding delegate method.
- [func predicate(forRow: Int) -> NSPredicate?](nsruleeditor/predicate(forrow:).md)
  Returns the predicate for a given row.
### Supporting Bindings
- [var rowClass: AnyClass](nsruleeditor/rowclass.md)
  The class used to create a new row in the “rows” binding.
- [var rowTypeKeyPath: String](nsruleeditor/rowtypekeypath.md)
  The key path for the row type.
- [var subrowsKeyPath: String](nsruleeditor/subrowskeypath.md)
  The key path for the subrows.
- [var criteriaKeyPath: String](nsruleeditor/criteriakeypath.md)
  The criteria key path.
- [var displayValuesKeyPath: String](nsruleeditor/displayvalueskeypath.md)
  The display values key path.
### Notifications
- [class let rowsDidChangeNotification: NSNotification.Name](nsruleeditor/rowsdidchangenotification.md)
  This notification is posted to the default notification center whenever the view’s rows change.

## Relationships

### Inherits From
- [NSControl](nscontrol.md)
### Inherited By
- [NSPredicateEditor](nspredicateeditor.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](nsappearancecustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](nstouchbarprovider.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Responding to control-based events using target-action](../UIKit/responding-to-control-based-events-using-target-action.md)
  Handle user input by connecting buttons, sliders, and other controls to your app’s code using the target-action design pattern.
- [class NSButton](nsbutton.md)
  A control that defines an area on the screen that a user clicks to trigger an action.
- [class NSColorWell](nscolorwell.md)
  A control that displays a color value and lets the user change that color value.
- [Combo Box](combo-box.md)
  Display a list of values in a pop-up menu that lets the user select a value or type in a custom value.
- [class NSComboButton](nscombobutton.md)
  A button with a pull-down menu and a default action.
- [Date Picker](date-picker.md)
  Display a calendar date and provide controls for editing the date value.
- [class NSImageView](nsimageview.md)
  A display of image data in a frame.
- [class NSLevelIndicator](nslevelindicator.md)
  A visual representation of a level or quantity, using discrete values.
- [Path Control](path-control.md)
  A display of a file system path or virtual path information.
- [class NSPopUpButton](nspopupbutton.md)
  A control for selecting an item from a list.
- [class NSProgressIndicator](nsprogressindicator.md)
  An interface that provides visual feedback to the user about the status of an ongoing task.
- [class NSPredicateEditor](nspredicateeditor.md)
  A defined set of rules that allows the editing of predicate objects.
- [Search Field](search-field.md)
  Provide a text field that is optimized for text-based search interfaces.
- [class NSSegmentedControl](nssegmentedcontrol.md)
  Display one or more buttons in a single horizontal group.
- [Slider](slider.md)
  Display a range of values from which the user selects a single value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor)*