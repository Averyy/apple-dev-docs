# birthday

**Framework**: Contacts  
**Kind**: property  
**Role**: Instance Property

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

*iOS, iPadOS, Mac Catalyst, visionOS, watchOS*

```objc
@property (nonatomic, copy, nullable) NSDateComponents * birthday;
```

*macOS*

```objc
@property (atomic, copy, nullable) NSDateComponents * birthday;
```

## Discussion

A Gregorian birthday can be displayed using this property, whose values are the relevant properties of an [`NSDateComponents`](../../Foundation/nsdatecomponents.md) object. Day and month are required for this property, and year is optional. Calendar can be `nil` or Gregorian. All other date components are invalid.

## See Also

### Setting Birthday Information
- [var dates: [CNLabeledValue<NSDateComponents>]](./dates.md)
  An array containing labeled Gregorian dates.
- [var nonGregorianBirthday: DateComponents?](./nongregorianbirthday.md)
  A date component for the non-Gregorian birthday of the contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnmutablecontact/birthday)*