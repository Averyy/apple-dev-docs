# parentContainer

**Framework**: Contacts UI  
**Kind**: property

The container in which to add a new contact.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var parentContainer: CNContainer? { get set }
```

#### Discussion

If you do not set this property, the view controller adds a new contact to the default container.

## See Also

- [var parentGroup: CNGroup?](cncontactviewcontroller/parentgroup.md)
  The group in which to add a new contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactviewcontroller/parentcontainer)*