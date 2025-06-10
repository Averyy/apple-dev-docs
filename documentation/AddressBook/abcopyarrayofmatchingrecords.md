# ABCopyArrayOfMatchingRecords(_:_:)

**Framework**: Address Book  
**Kind**: func

Returns an array of records that match the given search element, or an empty array if no records match the search element.

**Availability**:
- macOS ?+

## Declaration

```swift
func ABCopyArrayOfMatchingRecords(_ addressBook: ABAddressBookRef!, _ search: ABSearchElementRef!) -> Unmanaged<CFArray>!
```

#### Return Value

A new array containing ABRecord objects representing all the records that match `search`. If no records match `search`, this function returns an empty array. You are responsible for releasing this object.

## Parameters

- `addressBook`: The address book for the logged-in user.
- `search`: The search element that specifies the query. If   is  , this function raises an exception. Create an ABSearchElement object using the record specific functions:   or  . See   for more functions that create compound queries.

## See Also

- [func ABSearchElementCreateWithConjunction(ABSearchConjunction, CFArray!) -> Unmanaged<ABSearchElementRef>!](absearchelementcreatewithconjunction(_:_:).md)
  Returns a compound search element created by combiningthe search elements in an array with the given conjunction.
- [func ABSearchElementMatchesRecord(ABSearchElementRef!, ABRecordRef!) -> Bool](absearchelementmatchesrecord(_:_:).md)
  Tests whether or not a record matches a search element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abcopyarrayofmatchingrecords(_:_:))*