# ABPickerSelectIdentifier

**Framework**: Address Book  
**Kind**: func  
**Role**: Function

Selects a value or a set of values in a multi-value property.

**Availability**:
- macOS 10.3+

## Declaration

```c
extern void ABPickerSelectIdentifier(ABPickerRef inPicker, ABPersonRef inPerson, CFStringRef inIdentifier, bool inExtendSelection);
```

## Parameters

- `inPicker`: The people-picker window to manipulate.
- `inPerson`: The person with the multi-value property with the value to select.
- `inIdentifier`: The identifier of the value to select in the multi-value property.
- `inExtendSelection`: `true` if you want to add the value to the list of selected values in the multi-value property of the desired person; `false` if you want the value to be the only value selected in the list.

## See Also

### Functions
- [ABPickerAddProperty](./abpickeraddproperty.md)
  Adds a property to the group of properties available in the record list. Use [`ABPickerRemoveProperty`](./abpickerremoveproperty.md) to remove a property from the list and [`ABPickerCopyProperties`](./abpickercopyproperties.md) to obtain the list of properties available in the list.
- [ABPickerChangeAttributes](./abpickerchangeattributes.md)
  Specifies the selection behaviors for a people-picker window. Use `ABPickerGetAttributes` to obtain the selection behaviors specified for the window.
- [ABPickerClearSearchField](./abpickerclearsearchfield.md)
  Clears the search field and resets the list of displayed records.
- [ABPickerCopyColumnTitle](./abpickercopycolumntitle.md)
  Obtains the title of a custom property.
- [ABPickerCopyDisplayedProperty](./abpickercopydisplayedproperty.md)
  Returns the name of the property currently displayed in the record list.
- [ABPickerCopyProperties](./abpickercopyproperties.md)
  Obtains the list of properties available in the record list. Use [`ABPickerAddProperty`](./abpickeraddproperty.md) to add a property to the record list and [`ABPickerRemoveProperty`](./abpickerremoveproperty.md) to remove a property from the list.
- [ABPickerCopySelectedGroups](./abpickercopyselectedgroups.md)
  Returns the groups selected in the group list as an array of `ABRecord C` objects.
- [ABPickerCopySelectedIdentifiers](./abpickercopyselectedidentifiers.md)
  Returns the identifiers of the selected values in a multi-value property or an empty array if the property displayed is a single-value property.
- [ABPickerCopySelectedRecords](./abpickercopyselectedrecords.md)
  Returns the selection in the record list as an array of ABGroup or `ABPerson C` objects.
- [ABPickerCopySelectedValues](./abpickercopyselectedvalues.md)
  Returns the selected values in a multi-value property or an empty array if no values are selected or the property displayedis a single-value property.
- [ABPickerCreate](./abpickercreate.md)
  Creates an ABPickerRef. The corresponding window is hidden. Invoke [`ABPickerSetVisibility`](./abpickersetvisibility.md) to show it. Release with `CFRelease`.
- [ABPickerDeselectAll](./abpickerdeselectall.md)
  Deselects all selected groups, records, and values in multi-value properties.
- [ABPickerDeselectGroup](./abpickerdeselectgroup.md)
  Deselects a group in the group list.
- [ABPickerDeselectIdentifier](./abpickerdeselectidentifier.md)
  Deselects a value in multi-value property currently displayed in the record list.
- [ABPickerDeselectRecord](./abpickerdeselectrecord.md)
  Deselects a group in the record list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpickerselectidentifier)*