# displayedKeys

**Framework**: Contacts UI  
**Kind**: property  
**Role**: Instance Property

The keys to be displayed when a contact is expanded.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var displayedKeys: [String] { get set }
```

```objc
@property (copy) NSArray<NSString *> * displayedKeys;
```

#### Discussion

If no keys are provided, the picker selects contacts instead of values. For a list of possible keys, see [Contact Keys](../../Contacts/contact-keys.md).

## See Also

### Related Documentation
- [class CNContact](../../Contacts/cncontact.md)
  An immutable object that stores information about a single contact, such as the contact’s first name, phone numbers, and addresses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactpicker/displayedkeys)*