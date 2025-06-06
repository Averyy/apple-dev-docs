# shouldShowLinkedPeople

**Framework**: Address Book UI  
**Kind**: property

Indicates whether the person view should display data from person records that are linked with the person record being displayed.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var shouldShowLinkedPeople: Bool { get set }
```

#### Discussion

Linked records represent the same actual person. They often come from different sources, but may also come from the same source.

## See Also

- [var displayedPerson: ABRecord](abpersonviewcontroller/displayedperson.md)
  The person displayed by the person view.
- [var displayedProperties: [NSNumber]?](abpersonviewcontroller/displayedproperties.md)
  Identifies the set of properties (such as name or telephone number) of [`displayedPerson`](abpersonviewcontroller/displayedperson.md) the receiver displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abpersonviewcontroller/shouldshowlinkedpeople)*