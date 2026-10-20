# remove(_:)

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Removes an `ABPerson` or `ABGroup` record from the Address Book database.

**Availability**:
- macOS

## Declaration

```swift
func remove(_ record: ABRecord!) -> Bool
```

```objc
- (BOOL) removeRecord:(ABRecord *) record;
```

#### Return Value

`true` if the record was removed successfully; otherwise, `false`.

#### Discussion

If `record` is `nil`, this method raises an exception. Your changes are not committed until you call the [`save()`](./save%28%29.md) method.

## Parameters

- `record`: The record to be removed.

## See Also

### Adding and Removing Records
- [func add(ABRecord!, error: ()) throws](./add%28_,error%29.md)
  Adds an `ABPerson` or `ABGroup` record to the Address Book database.
- [func add(ABRecord!) -> Bool](./add%28_%29.md)
  Adds an `ABPerson` or `ABGroup` record to the Address Book database.
- [func remove(ABRecord!, error: ()) throws](./remove%28_,error%29.md)
  Removes an `ABPerson` or `ABGroup` record from the Address Book database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abaddressbook-swift.class/remove(_:))*