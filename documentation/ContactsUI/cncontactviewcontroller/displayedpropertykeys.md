# displayedPropertyKeys

**Framework**: Contacts UI  
**Kind**: property

The contact property keys to display.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var displayedPropertyKeys: [Any]? { get set }
```

#### Discussion

If this property is not set, the view controller displays all properties.

## See Also

- [var contact: CNContact](cncontactviewcontroller/contact.md)
  The contact being displayed.
- [var alternateName: String?](cncontactviewcontroller/alternatename.md)
  The name to use if the contact has no display name.
- [var message: String?](cncontactviewcontroller/message.md)
  The message displayed under the name of the contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactviewcontroller/displayedpropertykeys)*