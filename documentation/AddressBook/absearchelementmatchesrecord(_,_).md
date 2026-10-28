# ABSearchElementMatchesRecord(_:_:)

**Framework**: Address Book  
**Kind**: func  
**Role**: Function

Tests whether or not a record matches a search element.

**Availability**:
- macOS

## Declaration

```swift
func ABSearchElementMatchesRecord(_ searchElement: ABSearchElementRef!, _ record: ABRecordRef!) -> Bool
```

```c
extern bool ABSearchElementMatchesRecord(ABSearchElementRef searchElement, ABRecordRef record);
```

## Return Value

Returns `true` ifthe `record` parameter satisfies theconditions in the `searchElement`, `false` otherwise.

## Parameters

- `searchElement`: The search element containing the query you wish to test `record` with.
- `record`: The record you wish to test.

## See Also

### Search Elements
- [func ABCopyArrayOfMatchingRecords(ABAddressBookRef!, ABSearchElementRef!) -> Unmanaged<CFArray>!](./abcopyarrayofmatchingrecords%28_,_%29.md)
  Returns an array of records that match the given search element, or an empty array if no records match the search element.
- [func ABSearchElementCreateWithConjunction(ABSearchConjunction, CFArray!) -> Unmanaged<ABSearchElementRef>!](./absearchelementcreatewithconjunction%28_,_%29.md)
  Returns a compound search element created by combiningthe search elements in an array with the given conjunction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/absearchelementmatchesrecord(_:_:))*