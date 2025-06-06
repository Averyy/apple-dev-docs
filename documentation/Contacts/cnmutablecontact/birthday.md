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
var birthday: DateComponents? { get set }
```

#### Discussion

A Gregorian birthday can be displayed using this property, whose values are the relevant properties of an [`NSDateComponents`](https://developer.apple.com/documentation/Foundation/NSDateComponents) object. Day and month are required for this property, and year is optional. Calendar can be `nil` or Gregorian. All other date components are invalid.

## See Also

- [var dates: [CNLabeledValue<NSDateComponents>]](cnmutablecontact/dates.md)
  An array containing labeled Gregorian dates.
- [var nonGregorianBirthday: DateComponents?](cnmutablecontact/nongregorianbirthday.md)
  A date component for the non-Gregorian birthday of the contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnmutablecontact/birthday)*