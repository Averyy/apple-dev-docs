# contactViewController(_:shouldPerformDefaultActionFor:)

**Framework**: Contacts UI  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) contactViewController:(CNContactViewController *) viewController shouldPerformDefaultActionForContactProperty:(CNContactProperty *) property;
```

#### Return Value

[`true`](../../Swift/true.md) to call the default action performed for the property, otherwise return [`false`](../../Swift/false.md).

#### Discussion

Implement this method to determine the resulting behavior when a property is selected. Return [`false`](../../Swift/false.md) if you do not want anything to be done or if you are handling the actions yourself.

## Parameters

- `viewController`: The view controller presenting the contact.
- `property`: The property ([`CNContactProperty`](../../Contacts/cncontactproperty.md)) selected by the user.

## See Also

### Responding to User Events
- [func contactViewController(CNContactViewController, didCompleteWith: CNContact?)](./contactviewcontroller%28_,didcompletewith%29.md)
  Called when the view has been presented.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactviewcontrollerdelegate/contactviewcontroller(_:shouldperformdefaultactionfor:))*