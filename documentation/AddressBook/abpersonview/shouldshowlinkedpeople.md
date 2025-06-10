# shouldShowLinkedPeople

**Framework**: Address Book  
**Kind**: property

Indicates whether the person view should display data from person records that are linked with the person record being displayed.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
var shouldShowLinkedPeople: Bool { get set }
```

#### Discussion

Linked records represent the same actual person, and typically come from different sources.

## See Also

- [var editing: Bool](abpersonview/editing.md)
  A Boolean value that indicates whether the person view is in editing mode.
- [var person: ABPerson!](abpersonview/person.md)
  The contact record being displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpersonview/shouldshowlinkedpeople)*