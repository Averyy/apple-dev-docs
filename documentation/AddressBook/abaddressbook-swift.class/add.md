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

If the `record` argument is `nil`, this method raises an exception. Your changes are not committed until you call the [`save()`](abaddressbook-swift.class/save().md) method.

It is more efficient to use the  [`ABRecord`](abrecord-swift.class.md) method [`init(addressBook:)`](abrecord-swift.class/init(addressbook:).md) when possible.

## Parameters

- `record`: The record to add.

## See Also

- [func add(ABRecord!, error: ()) throws](abaddressbook-swift.class/add(_:error:).md)
  Adds an `ABPerson` or `ABGroup` record to the Address Book database.
- [func remove(ABRecord!, error: ()) throws](abaddressbook-swift.class/remove(_:error:).md)
  Removes an `ABPerson` or `ABGroup` record from the Address Book database.
- [func remove(ABRecord!) -> Bool](abaddressbook-swift.class/remove(_:).md)
  Removes an `ABPerson` or `ABGroup` record from the Address Book database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abaddressbook-swift.class/add(_:))*