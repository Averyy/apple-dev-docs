# predicateForSelectionOfContact

**Framework**: Contacts UI  
**Kind**: property

A predicate to control the return of the selected contact.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var predicateForSelectionOfContact: NSPredicate? { get set }
```

#### Discussion

This property determines whether a selected contact should be returned (when the predicate evaluates to TRUE), or a default action for the property should be performed (when the predicate evaluates to FALSE). By default the contact picker view controller displays the contact’s detail card when a contact is selected. To learn about predicates, see [`NSPredicate`](https://developer.apple.com/documentation/Foundation/NSPredicate).

## See Also

- [var predicateForEnablingContact: NSPredicate?](cncontactpickerviewcontroller/predicateforenablingcontact.md)
  A predicate to determine the contact selectability in the list of contacts.
- [var predicateForSelectionOfProperty: NSPredicate?](cncontactpickerviewcontroller/predicateforselectionofproperty.md)
  A predicate to control the properties of the selected contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactpickerviewcontroller/predicateforselectionofcontact)*