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
var dates: [CNLabeledValue<NSDateComponents>] { get set }
```

#### Discussion

This property is an array of [`CNLabeledValue`](cnlabeledvalue.md) objects, each of which has an [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) label and [`NSDateComponents`](https://developer.apple.com/documentation/Foundation/NSDateComponents) value. You can use this property to store Gregorian dates such as anniversaries. Day and month are required and year is optional. Calendar is `nil` or Gregorian. All other date components are invalid.

## See Also

- [var nonGregorianBirthday: DateComponents?](cnmutablecontact/nongregorianbirthday.md)
  A date component for the non-Gregorian birthday of the contact.
- [var birthday: DateComponents?](cnmutablecontact/birthday.md)
  A date component for the Gregorian birthday of the contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnmutablecontact/dates)*