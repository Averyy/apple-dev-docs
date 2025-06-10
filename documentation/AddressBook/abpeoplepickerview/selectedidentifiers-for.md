# selectedIdentifiers(for:)

**Framework**: Address Book  
**Kind**: method

Returns the identifiers of the selected values in a multivalue property.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func selectedIdentifiers(for person: ABPerson!) -> [Any]!
```

#### Discussion

Returns `nil` if the property displayed is a single-value property, or if the selected value is not a property of `person`.

The [`selectedRecords`](abpeoplepickerview/selectedrecords.md) property returns all of the person records that were unified to display the selected records, which can require some extra care in passing the correct person record.

## Parameters

- `person`: The person whose identifiers for selected values will be returned.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpeoplepickerview/selectedidentifiers(for:))*