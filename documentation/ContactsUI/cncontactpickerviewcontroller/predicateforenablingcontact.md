# predicateForEnablingContact

**Framework**: Contacts UI  
**Kind**: property

A predicate to determine the contact selectability in the list of contacts.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var predicateForEnablingContact: NSPredicate? { get set }
```

#### Discussion

You can set a value for this property to determine which contact should become selectable, such as `emailAddresses.@count > 0` to enable all the contacts that have an email address to become selectable. If no predicate is set for this property, all contacts become selectable. To learn about predicate syntax, see [`NSPredicate`](https://developer.apple.com/documentation/Foundation/NSPredicate).

## See Also

- [var predicateForSelectionOfContact: NSPredicate?](cncontactpickerviewcontroller/predicateforselectionofcontact.md)
  A predicate to control the return of the selected contact.
- [var predicateForSelectionOfProperty: NSPredicate?](cncontactpickerviewcontroller/predicateforselectionofproperty.md)
  A predicate to control the properties of the selected contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactpickerviewcontroller/predicateforenablingcontact)*