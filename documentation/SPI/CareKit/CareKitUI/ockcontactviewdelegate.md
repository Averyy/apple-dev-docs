---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockcontactviewdelegate"
framework: "CareKit/CareKitUI"
---

# OCKContactViewDelegate

**Framework**: CareKit/CareKitUI  
**Kind**: protocol  
**Role**: Protocol

A protocol that handles events related to a contact object.

## Declaration

```swift
protocol OCKContactViewDelegate : AnyObject
```

## Topics

### Instance Methods
- [func contactView(UIView & OCKContactDisplayable, senderDidInitiateAddressLookup: Any?)](./ockcontactviewdelegate/contactview%28_,senderdidinitiateaddresslookup%29.md)
  Called when the user would like to view the address of the contact.
- [func contactView(UIView & OCKContactDisplayable, senderDidInitiateCall: Any?)](./ockcontactviewdelegate/contactview%28_,senderdidinitiatecall%29.md)
  Called when the user would like to call the contact.
- [func contactView(UIView & OCKContactDisplayable, senderDidInitiateEmail: Any?)](./ockcontactviewdelegate/contactview%28_,senderdidinitiateemail%29.md)
  Called when the user would like to email the contact.
- [func contactView(UIView & OCKContactDisplayable, senderDidInitiateMessage: Any?)](./ockcontactviewdelegate/contactview%28_,senderdidinitiatemessage%29.md)
  Called when the user would like to message the contact.
- [func didSelectContactView(UIView & OCKContactDisplayable)](./ockcontactviewdelegate/didselectcontactview%28_%29.md)
  Called when the view displaying the contact was selected.

## See Also

### Contact-interaction broadcasting
- [protocol OCKContactDisplayable](./ockcontactdisplayable.md)
  Objects that display and handle interactions with a contact.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockcontactviewdelegate)*