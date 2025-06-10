# ABMultiValueReplaceLabel(_:_:_:)

**Framework**: Address Book  
**Kind**: func

Replaces the label at the given index.

**Availability**:
- macOS ?+

## Declaration

```swift
func ABMultiValueReplaceLabel(_ multiValue: ABMutableMultiValueRef!, _ label: CFString!, _ index: CFIndex) -> Bool
```

#### Return Value

`true` ifsuccessfully, `false` otherwise.

## Parameters

- `multiValue`: The multi-value list you wish to modify.
- `label`: The new label at  —it need not be unique. If   is  , this function raises an exception.
- `index`: The index of the entry to be modified. If   is out of bounds, this function raises an exception.

## See Also

- [func ABMultiValueAdd(ABMutableMultiValueRef!, CFTypeRef!, CFString!, UnsafeMutablePointer<Unmanaged<CFString>?>!) -> Bool](abmultivalueadd(_:_:_:_:).md)
  Adds a value and its label to a multi-value list.
- [func ABMultiValueCopyIdentifierAtIndex(ABMultiValueRef!, CFIndex) -> Unmanaged<CFString>!](abmultivaluecopyidentifieratindex(_:_:).md)
  Returns the identifier at the given index.
- [func ABMultiValueCopyLabelAtIndex(ABMultiValue!, CFIndex) -> Unmanaged<CFString>!](abmultivaluecopylabelatindex(_:_:).md)
  Returns the label for the given index.
- [func ABMultiValueCopyPrimaryIdentifier(ABMultiValueRef!) -> Unmanaged<CFString>!](abmultivaluecopyprimaryidentifier(_:).md)
  Returns the identifier for the primary value.
- [func ABMultiValueCopyValueAtIndex(ABMultiValue!, CFIndex) -> Unmanaged<CFTypeRef>!](abmultivaluecopyvalueatindex(_:_:).md)
  Returns the value for the given index.
- [func ABMultiValueCount(ABMultiValueRef!) -> CFIndex](abmultivaluecount(_:).md)
  Returns the number of entries in a multi-value list.
- [func ABMultiValueCreate() -> Unmanaged<ABMultiValueRef>!](abmultivaluecreate().md)
  Returns a new ABMultiValue object.
- [func ABMultiValueCreateCopy(ABMultiValueRef!) -> Unmanaged<ABMultiValueRef>!](abmultivaluecreatecopy(_:).md)
  Returns a copy of a multi-value object.
- [func ABMultiValueCreateMutable(ABPropertyType) -> Unmanaged<ABMutableMultiValue>!](abmultivaluecreatemutable().md)
  Returns a newly created mutable multi-value list object.
- [func ABMultiValueCreateMutableCopy(ABMultiValue!) -> Unmanaged<ABMutableMultiValue>!](abmultivaluecreatemutablecopy(_:).md)
  Returns a mutable copy of a multi-value object.
- [func ABMultiValueIndexForIdentifier(ABMultiValueRef!, CFString!) -> CFIndex](abmultivalueindexforidentifier(_:_:).md)
  Returns the index for the given identifier.
- [func ABMultiValueInsert(ABMutableMultiValueRef!, CFTypeRef!, CFString!, CFIndex, UnsafeMutablePointer<Unmanaged<CFString>?>!) -> Bool](abmultivalueinsert(_:_:_:_:_:).md)
  Inserts a value and its label at the given index in amulti-value list.
- [func ABMultiValuePropertyType(ABMultiValueRef!) -> ABPropertyType](abmultivaluepropertytype(_:).md)
  Returns the type for the values in a multi-value list.
- [func ABMultiValueRemove(ABMutableMultiValueRef!, CFIndex) -> Bool](abmultivalueremove(_:_:).md)
  Removes the value and label at the given index.
- [func ABMultiValueReplaceValue(ABMutableMultiValueRef!, CFTypeRef!, CFIndex) -> Bool](abmultivaluereplacevalue(_:_:_:).md)
  Replaces the value at the given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abmultivaluereplacelabel(_:_:_:))*