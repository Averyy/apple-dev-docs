# contactViewController(_:didCompleteWith:)

**Framework**: Contacts UI  
**Kind**: method

Called when the view has been presented.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func contactViewController(_ viewController: CNContactViewController, didCompleteWith contact: CNContact?)
```

#### Discussion

If creating a new contact, the new contact added to the contacts list is passed in `contact`. If adding to an existing contact, the existing contact is passed in `contact`. It is up to the delegate to dismiss the view controller.

## Parameters

- `viewController`: The view controller presenting the contact.
- `contact`: The newly, or existing contact being added.

## See Also

- [func contactViewController(CNContactViewController, shouldPerformDefaultActionFor: CNContactProperty) -> Bool](cncontactviewcontrollerdelegate/contactviewcontroller(_:shouldperformdefaultactionfor:).md)
  Called when the user selects a property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactviewcontrollerdelegate/contactviewcontroller(_:didcompletewith:))*