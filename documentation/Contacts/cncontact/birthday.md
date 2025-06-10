# birthday

**Framework**: Contacts  
**Kind**: property

A date component for the Gregorian birthday of the contact.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var birthday: DateComponents? { get }
```

#### Discussion

Birthdays are represented by this property, whose values are the relevant properties of an [`NSDateComponents`](https://developer.apple.com/documentation/Foundation/NSDateComponents) object. Day and month components are required for this property, and year is optional. The calendar component can be `nil` or [`gregorian`](https://developer.apple.com/documentation/Foundation/NSCalendar/Identifier/gregorian). All other date components are invalid and including them results in an [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) object that includes the key paths of the invalid components and the error code [`CNError.Code.validationConfigurationError`](cnerror/code/validationconfigurationerror.md).

## See Also

- [var nonGregorianBirthday: DateComponents?](cncontact/nongregorianbirthday.md)
  A date component for the non-Gregorian birthday of the contact.
- [var dates: [CNLabeledValue<NSDateComponents>]](cncontact/dates.md)
  An array containing labeled Gregorian dates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontact/birthday)*