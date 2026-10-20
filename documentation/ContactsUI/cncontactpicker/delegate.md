# delegate

**Framework**: Contacts UI  
**Kind**: property  
**Role**: Instance Property

The picker delegate to be notified when the user chooses a contact.

**Availability**:
- macOS 10.11+

## Declaration

```swift
weak var delegate: (any CNContactPickerDelegate)? { get set }
```

```objc
@property (weak) id<CNContactPickerDelegate> delegate;
```

## See Also

### Responding to Picker Interactions
- [protocol CNContactPickerDelegate](../cncontactpickerdelegate.md)
  The methods that you implement to respond to contact-picker user events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactpicker/delegate)*