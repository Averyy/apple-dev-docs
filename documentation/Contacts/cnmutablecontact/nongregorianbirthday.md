# nonGregorianBirthday

**Framework**: Contacts  
**Kind**: property  
**Role**: Instance Property

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

*iOS, iPadOS, Mac Catalyst, visionOS, watchOS*

```objc
@property (nonatomic, copy, nullable) NSDateComponents * nonGregorianBirthday;
```

*macOS*

```objc
@property (atomic, copy, nullable) NSDateComponents * nonGregorianBirthday;
```

#### Discussion

A non-Gregorian birthday such as Lunisolar birthdays can be displayed using this property, whose values are the relevant properties of an [`NSDateComponents`](../../Foundation/nsdatecomponents.md) object. Day and month are required; [`year`](../../Foundation/nsdatecomponents/year.md) and [`isLeapMonth`](../../Foundation/nsdatecomponents/isleapmonth.md) are optional. The calendar property is also required and must be non-Gregorian. Some supported calendars are Buddhist, Chinese, or Islamic. All other date components are invalid.

## See Also

### Setting Birthday Information
- [var dates: [CNLabeledValue<NSDateComponents>]](./dates.md)
  An array containing labeled Gregorian dates.
- [var birthday: DateComponents?](./birthday.md)
  A date component for the Gregorian birthday of the contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnmutablecontact/nongregorianbirthday)*