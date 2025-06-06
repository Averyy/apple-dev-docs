# displayedPerson

**Framework**: Address Book UI  
**Kind**: property

The person displayed by the person view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var displayedPerson: ABRecord { get set }
```

#### Discussion

The receiver displays the properties of this person record that are present in [`displayedProperties`](abpersonviewcontroller/displayedproperties.md).

## See Also

- [var displayedProperties: [NSNumber]?](abpersonviewcontroller/displayedproperties.md)
  Identifies the set of properties (such as name or telephone number) of [`displayedPerson`](abpersonviewcontroller/displayedperson.md) the receiver displays.
- [var shouldShowLinkedPeople: Bool](abpersonviewcontroller/shouldshowlinkedpeople.md)
  Indicates whether the person view should display data from person records that are linked with the person record being displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abpersonviewcontroller/displayedperson)*