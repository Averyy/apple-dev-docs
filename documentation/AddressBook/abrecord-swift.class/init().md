# init()

**Framework**: Address Book  
**Kind**: init  
**Role**: Initializer

Initializes a record using the shared address book.

**Availability**:
- macOS

## Declaration

```swift
init!()
```

```objc
- (id) init;
```

## Discussion

In macOS 10.5 and later, this is equivalent to `initWithAddressBook:[ABAddressBook addressBook]`.

## See Also

### Creating a Record
- [init!(addressBook: ABAddressBook!)](./init%28addressbook%29.md)
  Initializes a record using the given address book.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abrecord-swift.class/init())*