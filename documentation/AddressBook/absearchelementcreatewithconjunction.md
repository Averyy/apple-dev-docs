# ABSearchElementCreateWithConjunction(_:_:)

**Framework**: Address Book  
**Kind**: func

Returns a compound search element created by combiningthe search elements in an array with the given conjunction.

**Availability**:
- macOS ?+

## Declaration

```swift
func ABSearchElementCreateWithConjunction(_ conjunction: ABSearchConjunction, _ childrenSearchElement: CFArray!) -> Unmanaged<ABSearchElementRef>!
```

#### Return Value

A new compound searchelement joining the search elements in `children` using `conjunction`.You are responsible for releasing this object.

## Parameters

- `conjunction`: The conjunction used to join the search elements in  . Can be either   or  .
- `childrenSearchElement`: An array containing ABSearchElement objects to be joined using  . If   this function raises an exception.

## See Also

- [func ABCopyArrayOfMatchingRecords(ABAddressBookRef!, ABSearchElementRef!) -> Unmanaged<CFArray>!](abcopyarrayofmatchingrecords(_:_:).md)
  Returns an array of records that match the given search element, or an empty array if no records match the search element.
- [func ABSearchElementMatchesRecord(ABSearchElementRef!, ABRecordRef!) -> Bool](absearchelementmatchesrecord(_:_:).md)
  Tests whether or not a record matches a search element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/absearchelementcreatewithconjunction(_:_:))*