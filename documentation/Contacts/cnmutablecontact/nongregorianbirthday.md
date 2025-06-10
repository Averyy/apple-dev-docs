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
var nonGregorianBirthday: DateComponents? { get set }
```

#### Discussion

A non-Gregorian birthday such as Lunisolar birthdays can be displayed using this property, whose values are the relevant properties of an [`NSDateComponents`](https://developer.apple.com/documentation/Foundation/NSDateComponents) object. Day and month are required; [`year`](https://developer.apple.com/documentation/Foundation/NSDateComponents/year) and [`isLeapMonth`](https://developer.apple.com/documentation/Foundation/NSDateComponents/isLeapMonth) are optional. The calendar property is also required and must be non-Gregorian. Some supported calendars are Buddhist, Chinese, or Islamic. All other date components are invalid.

## See Also

- [var dates: [CNLabeledValue<NSDateComponents>]](cnmutablecontact/dates.md)
  An array containing labeled Gregorian dates.
- [var birthday: DateComponents?](cnmutablecontact/birthday.md)
  A date component for the Gregorian birthday of the contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnmutablecontact/nongregorianbirthday)*