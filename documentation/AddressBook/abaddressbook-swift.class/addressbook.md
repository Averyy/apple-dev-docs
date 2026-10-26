# addressBook

**Framework**: Address Book  
**Kind**: method  
**Role**: Type Method

Returns a new instance of `ABAddressBook`, or `nil` if the Address Book database can’t be initialized.

**Availability**:
- macOS 10.5+

## Declaration

```objc
+ (ABAddressBook *) addressBook;
```

#### Return Value

A new instance of `ABAddressBook`, or `nil` if the Address Book database can’t be initialized.

#### Discussion

If you’re just making one-off lookups and edits, the [`shared()`](./shared%28%29.md) method is probably more appropriate. If your code is executing a tight loop, the [`addressBook`](./addressbook.md) method can yield significant performance improvements when used with the [`ABPerson`](../abperson.md)  [`init(addressBook:)`](../abrecord-swift.class/init%28addressbook%29.md) method. See [Accessing the Address Book](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AddressBook/Tasks/ManagingGroups.html#//apple_ref/doc/uid/20001022-102346) for more details.

If the user denies your application access to the Address Book database, this method returns `nil`.

## See Also

### Creating and Initializing an Address Book
- [class func shared() -> ABAddressBook!](./shared%28%29.md)
  Returns the unique shared instance of `ABAddressBook`, or `nil` if the Address Book database can’t be initialized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abaddressbook-swift.class/addressbook)*