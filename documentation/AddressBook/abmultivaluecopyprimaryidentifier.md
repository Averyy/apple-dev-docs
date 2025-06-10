# ABMultiValueCopyPrimaryIdentifier(_:)

**Framework**: Address Book  
**Kind**: func

Returns the identifier for the primary value.

**Availability**:
- macOS ?+

## Declaration

```swift
func ABMultiValueCopyPrimaryIdentifier(_ multiValue: ABMultiValueRef!) -> Unmanaged<CFString>!
```

#### Return Value

The unique identifierfor the primary value. You are responsible for releasing this object.

#### Discussion

Use the [`ABMultiValueCopyIdentifierAtIndex(_:_:)`](abmultivaluecopyidentifieratindex(_:_:).md) functionto get index for the returned identifier, and the [`ABMultiValueCopyValueAtIndex(_:_:)`](abmultivaluecopyvalueatindex(_:_:).md)functionto get its value.

## Parameters

- `multiValue`: The multi-value list that you wish to access.

## See Also

- [func ABMultiValueAdd(ABMutableMultiValueRef!, CFTypeRef!, CFString!, UnsafeMutablePointer<Unmanaged<CFString>?>!) -> Bool](abmultivalueadd(_:_:_:_:).md)
  Adds a value and its label to a multi-value list.
- [func ABMultiValueCopyIdentifierAtIndex(ABMultiValueRef!, CFIndex) -> Unmanaged<CFString>!](abmultivaluecopyidentifieratindex(_:_:).md)
  Returns the identifier at the given index.
- [func ABMultiValueCopyLabelAtIndex(ABMultiValue!, CFIndex) -> Unmanaged<CFString>!](abmultivaluecopylabelatindex(_:_:).md)
  Returns the label for the given index.
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
- [func ABMultiValueReplaceLabel(ABMutableMultiValueRef!, CFString!, CFIndex) -> Bool](abmultivaluereplacelabel(_:_:_:).md)
  Replaces the label at the given index.
- [func ABMultiValueReplaceValue(ABMutableMultiValueRef!, CFTypeRef!, CFIndex) -> Bool](abmultivaluereplacevalue(_:_:_:).md)
  Replaces the value at the given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abmultivaluecopyprimaryidentifier(_:))*