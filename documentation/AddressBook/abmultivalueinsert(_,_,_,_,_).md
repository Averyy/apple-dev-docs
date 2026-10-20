# ABMultiValueInsert(_:_:_:_:_:)

**Framework**: Address Book  
**Kind**: func  
**Role**: Function

Inserts a value and its label at the given index in amulti-value list.

**Availability**:
- macOS

## Declaration

```swift
func ABMultiValueInsert(_ multiValue: ABMutableMultiValueRef!, _ value: CFTypeRef!, _ label: CFString!, _ index: CFIndex, _ outIdentifier: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> Bool
```

```c
extern bool ABMultiValueInsert(ABMutableMultiValueRef multiValue, CFTypeRef value, CFStringRef label, CFIndex index, CFStringRef*outIdentifier);
```

#### Return Value

`true` ifsuccessfully, `false` otherwise.

#### Discussion

This function performs no type checking and will let you adda value whose type does not match the types of the other valuesin the list. However, if you try to use a multi-value list whosevalues are not all of the same type, functions, such as the ABRecord [`ABRecordSetValue(_:_:_:_:)`](./abrecordsetvalue%28_,_,_,_%29.md) function,will returns `NULL` or kABErrorProperty.

## Parameters

- `multiValue`: The multi-value list you wish to modify.
- `value`: An object representing a value in a multi-value list–it must be of the correct type. For example, if `multiValue` is the value for a property of type kABMultiStringProperty, then `value` needs to be a CFString object. See Property Types for a list of supported types in a multi-value list(see descriptions of the `kABMulti...` constants). If `value` is `NULL`, this function raises an exception.
- `label`: The label for `value`—it need not be unique. If `label` is `NULL`, this function raises an exception.
- `index`: The index to insert `value` at. If `index` is out of bounds, this function raises an exception.
- `outIdentifier`: If `value` is added successfully, this parameter returns the new identifier.

## See Also

### Multi Values
- [func ABMultiValueAdd(ABMutableMultiValueRef!, CFTypeRef!, CFString!, UnsafeMutablePointer<Unmanaged<CFString>?>!) -> Bool](./abmultivalueadd%28_,_,_,_%29.md)
  Adds a value and its label to a multi-value list.
- [func ABMultiValueCopyIdentifierAtIndex(ABMultiValueRef!, CFIndex) -> Unmanaged<CFString>!](./abmultivaluecopyidentifieratindex%28_,_%29.md)
  Returns the identifier at the given index.
- [func ABMultiValueCopyLabelAtIndex(ABMultiValue!, CFIndex) -> Unmanaged<CFString>!](./abmultivaluecopylabelatindex%28_,_%29.md)
  Returns the label for the given index.
- [func ABMultiValueCopyPrimaryIdentifier(ABMultiValueRef!) -> Unmanaged<CFString>!](./abmultivaluecopyprimaryidentifier%28_%29.md)
  Returns the identifier for the primary value.
- [func ABMultiValueCopyValueAtIndex(ABMultiValue!, CFIndex) -> Unmanaged<CFTypeRef>!](./abmultivaluecopyvalueatindex%28_,_%29.md)
  Returns the value for the given index.
- [func ABMultiValueCount(ABMultiValueRef!) -> CFIndex](./abmultivaluecount%28_%29.md)
  Returns the number of entries in a multi-value list.
- [func ABMultiValueCreate() -> Unmanaged<ABMultiValueRef>!](./abmultivaluecreate%28%29.md)
  Returns a new ABMultiValue object.
- [func ABMultiValueCreateCopy(ABMultiValueRef!) -> Unmanaged<ABMultiValueRef>!](./abmultivaluecreatecopy%28_%29.md)
  Returns a copy of a multi-value object.
- [func ABMultiValueCreateMutable(ABPropertyType) -> Unmanaged<ABMutableMultiValue>!](./abmultivaluecreatemutable%28_%29.md)
  Returns a newly created mutable multi-value list object.
- [func ABMultiValueCreateMutableCopy(ABMultiValue!) -> Unmanaged<ABMutableMultiValue>!](./abmultivaluecreatemutablecopy%28_%29.md)
  Returns a mutable copy of a multi-value object.
- [func ABMultiValueIndexForIdentifier(ABMultiValueRef!, CFString!) -> CFIndex](./abmultivalueindexforidentifier%28_,_%29.md)
  Returns the index for the given identifier.
- [func ABMultiValuePropertyType(ABMultiValueRef!) -> ABPropertyType](./abmultivaluepropertytype%28_%29.md)
  Returns the type for the values in a multi-value list.
- [func ABMultiValueRemove(ABMutableMultiValueRef!, CFIndex) -> Bool](./abmultivalueremove%28_,_%29.md)
  Removes the value and label at the given index.
- [func ABMultiValueReplaceLabel(ABMutableMultiValueRef!, CFString!, CFIndex) -> Bool](./abmultivaluereplacelabel%28_,_,_%29.md)
  Replaces the label at the given index.
- [func ABMultiValueReplaceValue(ABMutableMultiValueRef!, CFTypeRef!, CFIndex) -> Bool](./abmultivaluereplacevalue%28_,_,_%29.md)
  Replaces the value at the given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abmultivalueinsert(_:_:_:_:_:))*