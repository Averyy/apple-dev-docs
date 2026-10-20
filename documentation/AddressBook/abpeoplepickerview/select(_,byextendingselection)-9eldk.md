# select(_:byExtendingSelection:)

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Selects a record or a set of records in the record list.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func select(_ record: ABRecord!, byExtendingSelection extend: Bool)
```

```objc
- (void) selectRecord:(ABRecord *) record byExtendingSelection:(BOOL) extend;
```

## Parameters

- `record`: The record to be selected, or to be added to the current selection.
- `extend`: [`true`](../../Swift/true.md) to extend the current selection; otherwise, [`false`](../../Swift/false.md).

## See Also

### Selecting Groups and Records
- [var allowsGroupSelection: Bool](./allowsgroupselection.md)
  A Boolean value that specifies whether the user can select entire groups in the group column.
- [var allowsMultipleSelection: Bool](./allowsmultipleselection.md)
  A Boolean value that specifies whether multiple groups, records, or values of multivalue properties can be selected at a time.
- [func deselectAll(Any!)](./deselectall%28_%29.md)
  Deselects all selected groups, records, and values in multivalue properties.
- [func deselect(ABGroup!)](./deselect%28_%29-3x7tl.md)
  Deselects a group selected in the group list.
- [func deselectIdentifier(String!, for: ABPerson!)](./deselectidentifier%28_,for%29.md)
  Deselects a value selected in a multivalue property.
- [func deselect(ABRecord!)](./deselect%28_%29-1yy11.md)
  Deselects a record selected in the record list.
- [var selectedGroups: [Any]!](./selectedgroups.md)
  The groups selected in the group list. (read-only)
- [func selectedIdentifiers(for: ABPerson!) -> [Any]!](./selectedidentifiers%28for%29.md)
  Returns the identifiers of the selected values in a multivalue property.
- [var selectedRecords: [Any]!](./selectedrecords.md)
  The selection in the records list. (read-only)
- [func selectedValues() -> [Any]!](./selectedvalues%28%29.md)
  Returns an array of all the values selected in the displayed multivalue property.
- [func select(ABGroup!, byExtendingSelection: Bool)](./select%28_,byextendingselection%29-6mrii.md)
  Selects a group or a set of groups in the group list.
- [func selectIdentifier(String!, for: ABPerson!, byExtendingSelection: Bool)](./selectidentifier%28_,for,byextendingselection%29.md)
  Selects a value or a set of values in a multivalue property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpeoplepickerview/select(_:byextendingselection:)-9eldk)*