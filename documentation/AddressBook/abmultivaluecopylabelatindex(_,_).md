# ABMultiValueCopyLabelAtIndex(_:_:)

**Framework**: Address Book  
**Kind**: func  
**Role**: Function

Returns the label for the given index.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS

> **Deprecated**: use [[NSArray objectAtIndex:] label] with the labeled value property

## Declaration

*iOS, iPadOS, Mac Catalyst*

```swift
func ABMultiValueCopyLabelAtIndex(_ multiValue: ABMultiValue!, _ index: CFIndex) -> Unmanaged<CFString>!
```

*macOS*

```swift
func ABMultiValueCopyLabelAtIndex(_ multiValue: ABMultiValueRef!, _ index: CFIndex) -> Unmanaged<CFString>!
```

```c
extern CFStringRefABMultiValueCopyLabelAtIndex(ABMultiValueRef multiValue, CFIndex index);
```

#### Return Value

The label at `index` in `multiValue`.You are responsible for releasing this object.

#### Discussion

Each value in a multi-value list must be the same type, andhas an associated pre-defined or user-defined label, and uniqueidentifier. Use the [`ABMultiValueCopyIdentifierAtIndex(_:_:)`](./abmultivaluecopyidentifieratindex%28_,_%29.md) functionto get a identifier, and the [`ABMultiValueCopyValueAtIndex(_:_:)`](./abmultivaluecopyvalueatindex%28_,_%29.md)functionto get a value.

## Parameters

- `multiValue`: The multi-value list that you wish to access.
- `index`: The index of the identifier you wish to obtain. If this parameter is out of bounds, this function raises an exception.

## See Also

### Multi Values
- [func ABMultiValueAdd(ABMutableMultiValueRef!, CFTypeRef!, CFString!, UnsafeMutablePointer<Unmanaged<CFString>?>!) -> Bool](./abmultivalueadd%28_,_,_,_%29.md)
  Adds a value and its label to a multi-value list.
- [func ABMultiValueCopyIdentifierAtIndex(ABMultiValueRef!, CFIndex) -> Unmanaged<CFString>!](./abmultivaluecopyidentifieratindex%28_,_%29.md)
  Returns the identifier at the given index.
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
- [func ABMultiValueRemove(ABMutableMultiValueRef!, CFIndex) -> Bool](./abmultivalueremove%28_,_%29.md)
  Removes the value and label at the given index.
- [func ABMultiValueReplaceLabel(ABMutableMultiValueRef!, CFString!, CFIndex) -> Bool](./abmultivaluereplacelabel%28_,_,_%29.md)
  Replaces the label at the given index.
- [func ABMultiValueReplaceValue(ABMutableMultiValueRef!, CFTypeRef!, CFIndex) -> Bool](./abmultivaluereplacevalue%28_,_,_%29.md)
  Replaces the value at the given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abmultivaluecopylabelatindex(_:_:))*