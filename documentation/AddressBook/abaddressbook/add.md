# add(_:)

**Framework**: Address Book  
**Kind**: method

Adds an `ABPerson` or `ABGroup` record to the Address Book database.

**Availability**:
- macOS ?+

## Declaration

```swift
func add(_ record: ABRecord!) -> Bool
```

#### Return Value

`true` if the record was added successfully; otherwise `false`.

#### Discussion

If the `record` argument is `nil`, this method raises an exception. Your changes are not committed until you call the [`save()`](abaddressbook/save().md) method.

It is more efficient to use the  [`ABRecord`](abrecord.md) method [`init(addressBook:)`](abrecord/init(addressbook:).md) when possible.

## Parameters

- `record`: The record to add.

## See Also

- [func add(ABRecord!, error: ()) throws](abaddressbook/add(_:error:).md)
  Adds an `ABPerson` or `ABGroup` record to the Address Book database.
- [func remove(ABRecord!, error: ()) throws](abaddressbook/remove(_:error:).md)
  Removes an `ABPerson` or `ABGroup` record from the Address Book database.
- [func remove(ABRecord!) -> Bool](abaddressbook/remove(_:).md)
  Removes an `ABPerson` or `ABGroup` record from the Address Book database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abaddressbook/add(_:))*