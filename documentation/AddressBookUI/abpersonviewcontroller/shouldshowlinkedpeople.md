# shouldShowLinkedPeople

**Framework**: Address Book UI  
**Kind**: property  
**Role**: Instance Property

Indicates whether the person view should display data from person records that are linked with the person record being displayed.

**Availability**:
- iOS 4.0+ - Deprecated in 9.0
- iPadOS 4.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`CNContactViewController`](../../ContactsUI/cncontactviewcontroller.md) instead.

## Declaration

```swift
var shouldShowLinkedPeople: Bool { get set }
```

```objc
@property (nonatomic) BOOL shouldShowLinkedPeople;
```

## Discussion

Linked records represent the same actual person. They often come from different sources, but may also come from the same source.

## See Also

### Displaying Person Properties
- [var displayedPerson: ABRecord](./displayedperson.md)
  The person displayed by the person view.
- [var displayedProperties: [NSNumber]?](./displayedproperties.md)
  Identifies the set of properties (such as name or telephone number) of [`displayedPerson`](./displayedperson.md) the receiver displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abpersonviewcontroller/shouldshowlinkedpeople)*