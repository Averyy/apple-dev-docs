# predicateForSelectionOfProperty

**Framework**: Contacts UI  
**Kind**: property

A predicate to control the properties of the selected contact.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var predicateForSelectionOfProperty: NSPredicate? { get set }
```

#### Discussion

This property determines whether a selected contact should be returned (when the predicate evaluates to TRUE), or a default action for the property should be performed (when the predicate evaluates to FALSE). By default the contact picker view controller returns the first selected property of the contact. This predicate is evaluated on the [`CNContactProperty`](https://developer.apple.com/documentation/Contacts/CNContactProperty) property that is being selected, such as `(key == 'emailAddresses') AND (value LIKE '*@apple.com')` to return email address of the contact if the address contains the string “@apple.com”.

## See Also

- [var predicateForEnablingContact: NSPredicate?](cncontactpickerviewcontroller/predicateforenablingcontact.md)
  A predicate to determine the contact selectability in the list of contacts.
- [var predicateForSelectionOfContact: NSPredicate?](cncontactpickerviewcontroller/predicateforselectionofcontact.md)
  A predicate to control the return of the selected contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactsui/cncontactpickerviewcontroller/predicateforselectionofproperty)*