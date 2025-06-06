# dates

**Framework**: Contacts  
**Kind**: property

An array containing labeled Gregorian dates.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var dates: [CNLabeledValue<NSDateComponents>] { get }
```

#### Discussion

This property is an array of [`CNLabeledValue`](cnlabeledvalue.md) objects, each of which has an [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) label and [`NSDateComponents`](https://developer.apple.com/documentation/Foundation/NSDateComponents) value. You can use this property to store Gregorian dates such as anniversaries. Day and month components are required and year is optional. The calendar component can be `nil` or [`gregorian`](https://developer.apple.com/documentation/foundation/nscalendar/identifier/1410488-gregorian). All other date components are invalid and including them results in an [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) object that includes the key paths of the invalid components and the error code [`CNError.Code.validationConfigurationError`](cnerror/code/validationconfigurationerror.md).

## See Also

- [var birthday: DateComponents?](cncontact/birthday.md)
  A date component for the Gregorian birthday of the contact.
- [var nonGregorianBirthday: DateComponents?](cncontact/nongregorianbirthday.md)
  A date component for the non-Gregorian birthday of the contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontact/dates)*