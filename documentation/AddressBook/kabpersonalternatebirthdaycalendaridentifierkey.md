# kABPersonAlternateBirthdayCalendarIdentifierKey

**Framework**: Address Book  
**Kind**: var  
**Role**: Global Variable

The associated value is a string representing the calendar identifier for a [`CFCalendar`](../CoreFoundation/cfcalendar.md).

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: use NSDateComponents.calendar

## Declaration

```swift
let kABPersonAlternateBirthdayCalendarIdentifierKey: CFString!
```

```c
extern CFStringRef const kABPersonAlternateBirthdayCalendarIdentifierKey;
```

## Discussion

Corresponds to [`calendar`](../Foundation/nsdatecomponents/calendar.md).

## See Also

### Deprecated
- [let kABPersonAddressCityKey: CFString!](./kabpersonaddresscitykey.md)
  City.
- [let kABPersonAddressCountryCodeKey: CFString!](./kabpersonaddresscountrycodekey.md)
  Country code. The value is an ISO country code.
- [let kABPersonAddressCountryKey: CFString!](./kabpersonaddresscountrykey.md)
  Country or region.
- [let kABPersonAddressProperty: ABPropertyID](./kabpersonaddressproperty.md)
  Identifier for the address multivalue property.
- [let kABPersonAddressStateKey: CFString!](./kabpersonaddressstatekey.md)
  State.
- [let kABPersonAddressStreetKey: CFString!](./kabpersonaddressstreetkey.md)
  Street.
- [let kABPersonAddressZIPKey: CFString!](./kabpersonaddresszipkey.md)
  Zip code.
- [let kABPersonAlternateBirthdayDayKey: CFString!](./kabpersonalternatebirthdaydaykey.md)
  The associated value is a [`CFNumber`](../CoreFoundation/cfnumber.md) of type [`CFNumberType.nsIntegerType`](../CoreFoundation/cfnumbertype/nsintegertype.md) whose value is the day for the birthday.
- [let kABPersonAlternateBirthdayEraKey: CFString!](./kabpersonalternatebirthdayerakey.md)
  The associated value is a [`CFNumber`](../CoreFoundation/cfnumber.md) of type [`CFNumberType.nsIntegerType`](../CoreFoundation/cfnumbertype/nsintegertype.md) whose value is the era for the birthday.
- [let kABPersonAlternateBirthdayIsLeapMonthKey: CFString!](./kabpersonalternatebirthdayisleapmonthkey.md)
  The associated value is a [`CFNumber`](../CoreFoundation/cfnumber.md) of type [`CFNumberType.charType`](../CoreFoundation/cfnumbertype/chartype.md).
- [let kABPersonAlternateBirthdayMonthKey: CFString!](./kabpersonalternatebirthdaymonthkey.md)
  The associated value is a [`CFNumber`](../CoreFoundation/cfnumber.md) of type [`CFNumberType.nsIntegerType`](../CoreFoundation/cfnumbertype/nsintegertype.md) whose value is the month for the birthday.
- [let kABPersonAlternateBirthdayProperty: ABPropertyID](./kabpersonalternatebirthdayproperty.md)
  The associated value is a [`kABDictionaryPropertyType`](./kabdictionarypropertytype.md) with keys specified by the other constants listed here.
- [let kABPersonAlternateBirthdayYearKey: CFString!](./kabpersonalternatebirthdayyearkey.md)
  The associated value is a [`CFNumber`](../CoreFoundation/cfnumber.md) of type [`CFNumberType.nsIntegerType`](../CoreFoundation/cfnumbertype/nsintegertype.md) whose value is the year for the birthday.
- [let kABPersonAnniversaryLabel: CFString!](./kabpersonanniversarylabel.md)
  Birthdate.
- [let kABPersonAssistantLabel: CFString!](./kabpersonassistantlabel.md)
  Assistant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/kabpersonalternatebirthdaycalendaridentifierkey)*