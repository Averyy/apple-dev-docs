# init(addressBook:)

**Framework**: Address Book  
**Kind**: init  
**Role**: Initializer

Initializes a record using the given address book.

**Availability**:
- macOS 10.5+

## Declaration

```swift
init!(addressBook: ABAddressBook!)
```

```objc
- (id) initWithAddressBook:(ABAddressBook *) addressBook;
```

## Discussion

The record is added to `addressBook` but is not visible to other address books until `addressBook` is saved. This method is the designated initializer for this class.

## Parameters

- `addressBook`: The address book with which to initialize the record.

## See Also

### Creating a Record
- [init!()](./init%28%29.md)
  Initializes a record using the shared address book.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abrecord-swift.class/init(addressbook:))*