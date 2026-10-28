# contactViewController(_:didCompleteWith:)

**Framework**: Contacts UI  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) contactViewController:(CNContactViewController *) viewController didCompleteWithContact:(CNContact *) contact;
```

## Discussion

If creating a new contact, the new contact added to the contacts list is passed in `contact`. If adding to an existing contact, the existing contact is passed in `contact`. It is up to the delegate to dismiss the view controller.

## Parameters

- `viewController`: The view controller presenting the contact.
- `contact`: The newly, or existing contact being added.

## See Also

### Responding to User Events
- [func contactViewController(CNContactViewController, shouldPerformDefaultActionFor: CNContactProperty) -> Bool](./contactviewcontroller%28_,shouldperformdefaultactionfor%29.md)
  Called when the user selects a property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactviewcontrollerdelegate/contactviewcontroller(_:didcompletewith:))*