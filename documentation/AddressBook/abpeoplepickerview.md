# ABPeoplePickerView

**Framework**: Address Book  
**Kind**: class

An object you use to customize the behavior of people-picker views in an app’s user interface.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
class ABPeoplePickerView
```

## Topics

### Working with Properties in the Record List
- [func addProperty(String!)](abpeoplepickerview/addproperty(_:).md)
  Adds a property to the group of properties whose values are shown in the record list.
- [func columnTitle(forProperty: String!) -> String!](abpeoplepickerview/columntitle(forproperty:).md)
  Returns the title of a custom property.
- [var displayedProperty: String!](abpeoplepickerview/displayedproperty.md)
  The property currently displayed in the record list.
- [func properties() -> [Any]!](abpeoplepickerview/properties.md)
  Returns an array of the properties whose values are shown in the record list.
- [func removeProperty(String!)](abpeoplepickerview/removeproperty(_:).md)
  Removes a property from the group of properties whose values are shown in the record list.
- [func setColumnTitle(String!, forProperty: String!)](abpeoplepickerview/setcolumntitle(_:forproperty:).md)
  Sets the title displayed in the people picker for a property.
### Specifying Selection Behavior
- [var valueSelectionBehavior: ABPeoplePickerSelectionBehavior](abpeoplepickerview/valueselectionbehavior.md)
  The current selection behavior.
- [struct ABPeoplePickerSelectionBehavior](abpeoplepickerselectionbehavior.md)
  Constants indicating the possible value selection behaviors.
### Selecting Groups and Records
- [var allowsGroupSelection: Bool](abpeoplepickerview/allowsgroupselection.md)
  A Boolean value that specifies whether the user can select entire groups in the group column.
- [var allowsMultipleSelection: Bool](abpeoplepickerview/allowsmultipleselection.md)
  A Boolean value that specifies whether multiple groups, records, or values of multivalue properties can be selected at a time.
- [func deselectAll(Any!)](abpeoplepickerview/deselectall(_:).md)
  Deselects all selected groups, records, and values in multivalue properties.
- [func deselect(ABGroup!)](abpeoplepickerview/deselect(_:)-3x7tl.md)
  Deselects a group selected in the group list.
- [func deselectIdentifier(String!, for: ABPerson!)](abpeoplepickerview/deselectidentifier(_:for:).md)
  Deselects a value selected in a multivalue property.
- [func deselect(ABRecord!)](abpeoplepickerview/deselect(_:)-1yy11.md)
  Deselects a record selected in the record list.
- [var selectedGroups: [Any]!](abpeoplepickerview/selectedgroups.md)
  The groups selected in the group list. (read-only)
- [func selectedIdentifiers(for: ABPerson!) -> [Any]!](abpeoplepickerview/selectedidentifiers(for:).md)
  Returns the identifiers of the selected values in a multivalue property.
- [var selectedRecords: [Any]!](abpeoplepickerview/selectedrecords.md)
  The selection in the records list. (read-only)
- [func selectedValues() -> [Any]!](abpeoplepickerview/selectedvalues.md)
  Returns an array of all the values selected in the displayed multivalue property.
- [func select(ABGroup!, byExtendingSelection: Bool)](abpeoplepickerview/select(_:byextendingselection:)-6mrii.md)
  Selects a group or a set of groups in the group list.
- [func selectIdentifier(String!, for: ABPerson!, byExtendingSelection: Bool)](abpeoplepickerview/selectidentifier(_:for:byextendingselection:).md)
  Selects a value or a set of values in a multivalue property.
- [func select(ABRecord!, byExtendingSelection: Bool)](abpeoplepickerview/select(_:byextendingselection:)-9eldk.md)
  Selects a record or a set of records in the record list.
### Specifying the Accessory View
- [var accessoryView: NSView!](abpeoplepickerview/accessoryview.md)
  The view that is placed to the left of the search field.
### Managing Actions
- [func clearSearchField(Any!)](abpeoplepickerview/clearsearchfield(_:).md)
  Clears the search field and resets the list of displayed records.
- [func editInAddressBook(Any!)](abpeoplepickerview/editinaddressbook(_:).md)
  Launches Address Book to edit the item selected in the people picker.
- [var groupDoubleAction: Selector!](abpeoplepickerview/groupdoubleaction.md)
  The action to be invoked when a group is double-clicked.
- [var nameDoubleAction: Selector!](abpeoplepickerview/namedoubleaction.md)
  The action to be invoked when a name is double-clicked.
- [func selectInAddressBook(Any!)](abpeoplepickerview/selectinaddressbook(_:).md)
  Launches Address Book and selects the item selected in the people picker.
- [var target: AnyObject!](abpeoplepickerview/target.md)
  The target for double-click actions.
### Managing Persistent User Settings
- [var autosaveName: String!](abpeoplepickerview/autosavename.md)
  The name under which the column positions and the filter selection are saved.

## Relationships

### Inherits From
- [NSView](../AppKit/NSView.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/NSAccessibilityElementProtocol.md)
- [NSAccessibilityProtocol](../AppKit/NSAccessibilityProtocol.md)
- [NSAnimatablePropertyContainer](../AppKit/NSAnimatablePropertyContainer.md)
- [NSAppearanceCustomization](../AppKit/NSAppearanceCustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](../AppKit/NSDraggingDestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class ABPersonView](abpersonview.md)
  An object that provides a view for displaying and editing contacts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpeoplepickerview)*