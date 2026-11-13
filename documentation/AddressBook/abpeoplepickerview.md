# ABPeoplePickerView

**Framework**: Address Book  
**Kind**: class  
**Role**: Class

An object you use to customize the behavior of people-picker views in an app’s user interface.

**Availability**:
- macOS 10.3+

## Declaration

```swift
class ABPeoplePickerView
```

```objc
@interface ABPeoplePickerView : NSView
```

## Topics

### Working with Properties in the Record List
- [func addProperty(String!)](./abpeoplepickerview/addproperty%28_%29.md)
  Adds a property to the group of properties whose values are shown in the record list.
- [func columnTitle(forProperty: String!) -> String!](./abpeoplepickerview/columntitle%28forproperty%29.md)
  Returns the title of a custom property.
- [var displayedProperty: String!](./abpeoplepickerview/displayedproperty.md)
  The property currently displayed in the record list.
- [func properties() -> [Any]!](./abpeoplepickerview/properties%28%29.md)
  Returns an array of the properties whose values are shown in the record list.
- [func removeProperty(String!)](./abpeoplepickerview/removeproperty%28_%29.md)
  Removes a property from the group of properties whose values are shown in the record list.
- [func setColumnTitle(String!, forProperty: String!)](./abpeoplepickerview/setcolumntitle%28_,forproperty%29.md)
  Sets the title displayed in the people picker for a property.
### Specifying Selection Behavior
- [var valueSelectionBehavior: ABPeoplePickerSelectionBehavior](./abpeoplepickerview/valueselectionbehavior.md)
  The current selection behavior.
- [struct ABPeoplePickerSelectionBehavior](./abpeoplepickerselectionbehavior.md)
  Constants indicating the possible value selection behaviors.
### Selecting Groups and Records
- [var allowsGroupSelection: Bool](./abpeoplepickerview/allowsgroupselection.md)
  A Boolean value that specifies whether the user can select entire groups in the group column.
- [var allowsMultipleSelection: Bool](./abpeoplepickerview/allowsmultipleselection.md)
  A Boolean value that specifies whether multiple groups, records, or values of multivalue properties can be selected at a time.
- [func deselectAll(Any!)](./abpeoplepickerview/deselectall%28_%29.md)
  Deselects all selected groups, records, and values in multivalue properties.
- [func deselect(ABGroup!)](./abpeoplepickerview/deselect%28_%29-3x7tl.md)
  Deselects a group selected in the group list.
- [func deselectIdentifier(String!, for: ABPerson!)](./abpeoplepickerview/deselectidentifier%28_,for%29.md)
  Deselects a value selected in a multivalue property.
- [func deselect(ABRecord!)](./abpeoplepickerview/deselect%28_%29-1yy11.md)
  Deselects a record selected in the record list.
- [var selectedGroups: [Any]!](./abpeoplepickerview/selectedgroups.md)
  The groups selected in the group list. (read-only)
- [func selectedIdentifiers(for: ABPerson!) -> [Any]!](./abpeoplepickerview/selectedidentifiers%28for%29.md)
  Returns the identifiers of the selected values in a multivalue property.
- [var selectedRecords: [Any]!](./abpeoplepickerview/selectedrecords.md)
  The selection in the records list. (read-only)
- [func selectedValues() -> [Any]!](./abpeoplepickerview/selectedvalues%28%29.md)
  Returns an array of all the values selected in the displayed multivalue property.
- [func select(ABGroup!, byExtendingSelection: Bool)](./abpeoplepickerview/select%28_,byextendingselection%29-6mrii.md)
  Selects a group or a set of groups in the group list.
- [func selectIdentifier(String!, for: ABPerson!, byExtendingSelection: Bool)](./abpeoplepickerview/selectidentifier%28_,for,byextendingselection%29.md)
  Selects a value or a set of values in a multivalue property.
- [func select(ABRecord!, byExtendingSelection: Bool)](./abpeoplepickerview/select%28_,byextendingselection%29-9eldk.md)
  Selects a record or a set of records in the record list.
### Specifying the Accessory View
- [var accessoryView: NSView!](./abpeoplepickerview/accessoryview.md)
  The view that is placed to the left of the search field.
### Managing Actions
- [func clearSearchField(Any!)](./abpeoplepickerview/clearsearchfield%28_%29.md)
  Clears the search field and resets the list of displayed records.
- [func editInAddressBook(Any!)](./abpeoplepickerview/editinaddressbook%28_%29.md)
  Launches Address Book to edit the item selected in the people picker.
- [var groupDoubleAction: Selector!](./abpeoplepickerview/groupdoubleaction.md)
  The action to be invoked when a group is double-clicked.
- [var nameDoubleAction: Selector!](./abpeoplepickerview/namedoubleaction.md)
  The action to be invoked when a name is double-clicked.
- [func selectInAddressBook(Any!)](./abpeoplepickerview/selectinaddressbook%28_%29.md)
  Launches Address Book and selects the item selected in the people picker.
- [var target: AnyObject!](./abpeoplepickerview/target.md)
  The target for double-click actions.
### Managing Persistent User Settings
- [var autosaveName: String!](./abpeoplepickerview/autosavename.md)
  The name under which the column positions and the filter selection are saved.
### Notifications
- [ABPeoplePickerGroupSelectionDidChangeNotification](./abpeoplepickergroupselectiondidchangenotification.md)
  Posted when the selection in the group list is changed.
- [ABPeoplePickerNameSelectionDidChangeNotification](./abpeoplepickernameselectiondidchangenotification.md)
  Posted when the selection in the name list is changed.
- [ABPeoplePickerValueSelectionDidChangeNotification](./abpeoplepickervalueselectiondidchangenotification.md)
  Posted when the selection in a multivalue property is changed.
- [ABPeoplePickerDisplayedPropertyDidChangeNotification](./abpeoplepickerdisplayedpropertydidchangenotification.md)
  Posted when the displayed property in the record list is changed.

## Relationships

### Inherits From
- [NSView](../AppKit/nsview.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../AppKit/nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](../AppKit/nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](../AppKit/nsappearancecustomization.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSDraggingDestination](../AppKit/nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/nsuserinterfaceitemidentification.md)

## See Also

### Pickers
- [class ABPersonView](./abpersonview.md)
  An object that provides a view for displaying and editing contacts.
- [ABPersonPicker](./abpersonpicker.md)
  A picker object that you display when you want the user to select contacts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpeoplepickerview)*