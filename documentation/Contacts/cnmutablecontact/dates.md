# dates

**Framework**: Contacts  
**Kind**: property  
**Role**: Instance Property

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

*iOS, iPadOS, Mac Catalyst, visionOS, watchOS*

```objc
@property (nonatomic, copy) NSArray<CNLabeledValue<NSDateComponents *> *> * dates;
```

*macOS*

```objc
@property (atomic, copy) NSArray<CNLabeledValue<NSDateComponents *> *> * dates;
```

#### Discussion

This property is an array of [`CNLabeledValue`](../cnlabeledvalue.md) objects, each of which has an [`NSString`](../../Foundation/nsstring.md) label and [`NSDateComponents`](../../Foundation/nsdatecomponents.md) value. You can use this property to store Gregorian dates such as anniversaries. Day and month are required and year is optional. Calendar is `nil` or Gregorian. All other date components are invalid.

## See Also

### Setting Birthday Information
- [var nonGregorianBirthday: DateComponents?](./nongregorianbirthday.md)
  A date component for the non-Gregorian birthday of the contact.
- [var birthday: DateComponents?](./birthday.md)
  A date component for the Gregorian birthday of the contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnmutablecontact/dates)*