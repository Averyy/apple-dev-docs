# parentGroup

**Framework**: Contacts UI  
**Kind**: property

The group in which to add a new contact.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var parentGroup: CNGroup? { get set }
```

#### Discussion

If you do not set this property, the view controller adds a new contact to the default group.

## See Also

- [var parentContainer: CNContainer?](cncontactviewcontroller/parentcontainer.md)
  The container in which to add a new contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactviewcontroller/parentgroup)*