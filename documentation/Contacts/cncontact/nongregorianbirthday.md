# nonGregorianBirthday

**Framework**: Contacts  
**Kind**: property

A date component for the non-Gregorian birthday of the contact.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var nonGregorianBirthday: DateComponents? { get }
```

#### Discussion

Non-Gregorian birthdays can be displayed using this property, which has values that are the relevant properties of an [`NSDateComponents`](https://developer.apple.com/documentation/Foundation/NSDateComponents) object. Day and month components are required; year and leap month are optional. The calendar component is also required and must be an [`NSCalendar`](https://developer.apple.com/documentation/Foundation/NSCalendar) object with an identifier other than [`gregorian`](https://developer.apple.com/documentation/foundation/nscalendar/identifier/1410488-gregorian). For example, some supported calendars are Chinese, Hebrew, or Islamic. All other date components are invalid and including them results in an [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) object that includes the key paths of the invalid components and the error code [`CNError.Code.validationConfigurationError`](cnerror/code/validationconfigurationerror.md).

## See Also

- [var birthday: DateComponents?](cncontact/birthday.md)
  A date component for the Gregorian birthday of the contact.
- [var dates: [CNLabeledValue<NSDateComponents>]](cncontact/dates.md)
  An array containing labeled Gregorian dates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontact/nongregorianbirthday)*