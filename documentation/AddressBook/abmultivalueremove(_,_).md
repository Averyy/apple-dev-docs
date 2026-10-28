# ABMultiValueRemove(_:_:)

**Framework**: Address Book  
**Kind**: func  
**Role**: Function

Removes the value and label at the given index.

**Availability**:
- macOS

## Declaration

```swift
func ABMultiValueRemove(_ multiValue: ABMutableMultiValueRef!, _ index: CFIndex) -> Bool
```

```c
extern bool ABMultiValueRemove(ABMutableMultiValueRef multiValue, CFIndex index);
```

## Return Value

`true` ifsuccessfully, `false` otherwise.

## Parameters

- `multiValue`: The multi-value list you wish to modify.
- `index`: The index of the entry to be removed. If `index` is out of bounds, this function raises an exception.

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
- [func ABMultiValueInsert(ABMutableMultiValueRef!, CFTypeRef!, CFString!, CFIndex, UnsafeMutablePointer<Unmanaged<CFString>?>!) -> Bool](./abmultivalueinsert%28_,_,_,_,_%29.md)
  Inserts a value and its label at the given index in amulti-value list.
- [func ABMultiValuePropertyType(ABMultiValueRef!) -> ABPropertyType](./abmultivaluepropertytype%28_%29.md)
  Returns the type for the values in a multi-value list.
- [func ABMultiValueReplaceLabel(ABMutableMultiValueRef!, CFString!, CFIndex) -> Bool](./abmultivaluereplacelabel%28_,_,_%29.md)
  Replaces the label at the given index.
- [func ABMultiValueReplaceValue(ABMutableMultiValueRef!, CFTypeRef!, CFIndex) -> Bool](./abmultivaluereplacevalue%28_,_,_%29.md)
  Replaces the value at the given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abmultivalueremove(_:_:))*