# displayedProperties

**Framework**: Address Book UI  
**Kind**: property  
**Role**: Instance Property

Identifies the set of properties (such as name or telephone number) of [`displayedPerson`](./displayedperson.md) the receiver displays.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`CNContactViewController`](../../ContactsUI/cncontactviewcontroller.md) instead.

## Declaration

```swift
var displayedProperties: [NSNumber]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSArray<NSNumber *> * displayedProperties;
```

#### Discussion

The default value of this property is `NULL`.

Name properties are always displayed.

The properties are specified using an array of [`NSNumber`](../../Foundation/nsnumber.md) objects representing [`ABPropertyID`](../../AddressBook/abpropertyid.md) values.

To have the receiver display a single property for [`displayedPerson`](./displayedperson.md), such as telephone number, set `displayedProperties` to an array with a single value, such as `kABPersonPhoneProperty`.

## See Also

### Displaying Person Properties
- [var displayedPerson: ABRecord](./displayedperson.md)
  The person displayed by the person view.
- [var shouldShowLinkedPeople: Bool](./shouldshowlinkedpeople.md)
  Indicates whether the person view should display data from person records that are linked with the person record being displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abpersonviewcontroller/displayedproperties)*