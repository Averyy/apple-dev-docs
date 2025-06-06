# displayedPropertyKeys

**Framework**: Contacts UI  
**Kind**: property

The [`CNContact`](https://developer.apple.com/documentation/Contacts/CNContact) property keys to display in the contact detail card.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var displayedPropertyKeys: [String]? { get set }
```

#### Discussion

All the properties of the contact are displayed if this property is not set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactpickerviewcontroller/displayedpropertykeys)*