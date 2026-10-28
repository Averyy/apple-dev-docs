# displayedPerson

**Framework**: Address Book UI  
**Kind**: property  
**Role**: Instance Property

The person displayed by the person view.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`CNContactViewController`](../../ContactsUI/cncontactviewcontroller.md) instead.

## Declaration

```swift
var displayedPerson: ABRecord { get set }
```

```objc
@property (nonatomic, readwrite) ABRecordRef displayedPerson;
```

## Discussion

The receiver displays the properties of this person record that are present in [`displayedProperties`](./displayedproperties.md).

## See Also

### Displaying Person Properties
- [var displayedProperties: [NSNumber]?](./displayedproperties.md)
  Identifies the set of properties (such as name or telephone number) of [`displayedPerson`](./displayedperson.md) the receiver displays.
- [var shouldShowLinkedPeople: Bool](./shouldshowlinkedpeople.md)
  Indicates whether the person view should display data from person records that are linked with the person record being displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abpersonviewcontroller/displayedperson)*