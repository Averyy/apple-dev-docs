# contactViewController(_:shouldPerformDefaultActionFor:)

**Framework**: Contacts UI  
**Kind**: method

Called when the user selects a property.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func contactViewController(_ viewController: CNContactViewController, shouldPerformDefaultActionFor property: CNContactProperty) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) to call the default action performed for the property, otherwise return [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

Implement this method to determine the resulting behavior when a property is selected. Return [`false`](https://developer.apple.com/documentation/swift/false) if you do not want anything to be done or if you are handling the actions yourself.

## Parameters

- `viewController`: The view controller presenting the contact.
- `property`: The property ( )   selected by the user.

## See Also

- [func contactViewController(CNContactViewController, didCompleteWith: CNContact?)](cncontactviewcontrollerdelegate/contactviewcontroller(_:didcompletewith:).md)
  Called when the view has been presented.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactviewcontrollerdelegate/contactviewcontroller(_:shouldperformdefaultactionfor:))*