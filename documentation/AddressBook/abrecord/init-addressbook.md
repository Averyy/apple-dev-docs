# init(addressBook:)

**Framework**: Address Book  
**Kind**: init

Initializes a record using the given address book.

**Availability**:
- macOS 10.5+

## Declaration

```swift
init!(addressBook: ABAddressBook!)
```

#### Discussion

The record is added to `addressBook` but is not visible to other address books until `addressBook` is saved. This method is the designated initializer for this class.

## Parameters

- `addressBook`: The address book with which to initialize the record.

## See Also

- [init!()](abrecord/init.md)
  Initializes a record using the shared address book.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abrecord/init(addressbook:))*