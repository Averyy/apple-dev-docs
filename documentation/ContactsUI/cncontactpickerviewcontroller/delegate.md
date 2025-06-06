# delegate

**Framework**: Contacts UI  
**Kind**: property

The delegate to be notified when the user selects a contact or a property.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any CNContactPickerDelegate)? { get set }
```

## See Also

- [protocol CNContactPickerDelegate](cncontactpickerdelegate.md)
  The methods that you implement to respond to contact-picker user events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactpickerviewcontroller/delegate)*