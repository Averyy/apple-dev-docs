# add(_:)

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Adds an `ABPerson` or `ABGroup` record to the Address Book database.

**Availability**:
- macOS

## Declaration

```swift
func add(_ record: ABRecord!) -> Bool
```

```objc
- (BOOL) addRecord:(ABRecord *) record;
```

#### Return Value

`true` if the record was added successfully; otherwise `false`.

#### Discussion

If the `record` argument is `nil`, this method raises an exception. Your changes are not committed until you call the [`save()`](./save%28%29.md) method.

It is more efficient to use the  [`ABRecord`](../abrecord-swift.class.md) method [`init(addressBook:)`](../abrecord-swift.class/init%28addressbook%29.md) when possible.

## Parameters

- `record`: The record to add.

## See Also

### Adding and Removing Records
- [func add(ABRecord!, error: ()) throws](./add%28_,error%29.md)
  Adds an `ABPerson` or `ABGroup` record to the Address Book database.
- [func remove(ABRecord!, error: ()) throws](./remove%28_,error%29.md)
  Removes an `ABPerson` or `ABGroup` record from the Address Book database.
- [func remove(ABRecord!) -> Bool](./remove%28_%29.md)
  Removes an `ABPerson` or `ABGroup` record from the Address Book database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abaddressbook-swift.class/add(_:))*