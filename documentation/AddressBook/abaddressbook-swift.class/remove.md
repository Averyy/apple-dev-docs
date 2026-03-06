# remove(_:)

**Framework**: Address Book  
**Kind**: method

Removes an `ABPerson` or `ABGroup` record from the Address Book database.

**Availability**:
- macOS ?+

## Declaration

```swift
func remove(_ record: ABRecord!) -> Bool
```

#### Return Value

`true` if the record was removed successfully; otherwise, `false`.

#### Discussion

If `record` is `nil`, this method raises an exception. Your changes are not committed until you call the [`save()`](abaddressbook-swift.class/save().md) method.

## Parameters

- `record`: The record to be removed.

## See Also

- [func add(ABRecord!, error: ()) throws](abaddressbook-swift.class/add(_:error:).md)
  Adds an `ABPerson` or `ABGroup` record to the Address Book database.
- [func add(ABRecord!) -> Bool](abaddressbook-swift.class/add(_:).md)
  Adds an `ABPerson` or `ABGroup` record to the Address Book database.
- [func remove(ABRecord!, error: ()) throws](abaddressbook-swift.class/remove(_:error:).md)
  Removes an `ABPerson` or `ABGroup` record from the Address Book database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abaddressbook-swift.class/remove(_:))*