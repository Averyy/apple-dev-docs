# displayedProperties

**Framework**: Address Book UI  
**Kind**: property

Identifies the set of properties (such as name or telephone number) of [`displayedPerson`](abpersonviewcontroller/displayedperson.md) the receiver displays.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var displayedProperties: [NSNumber]? { get set }
```

#### Discussion

The default value of this property is `NULL`.

Name properties are always displayed.

The properties are specified using an array of [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) objects representing [`ABPropertyID`](https://developer.apple.com/documentation/AddressBook/ABPropertyID) values.

To have the receiver display a single property for [`displayedPerson`](abpersonviewcontroller/displayedperson.md), such as telephone number, set `displayedProperties` to an array with a single value, such as `kABPersonPhoneProperty`.

## See Also

- [var displayedPerson: ABRecord](abpersonviewcontroller/displayedperson.md)
  The person displayed by the person view.
- [var shouldShowLinkedPeople: Bool](abpersonviewcontroller/shouldshowlinkedpeople.md)
  Indicates whether the person view should display data from person records that are linked with the person record being displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abpersonviewcontroller/displayedproperties)*