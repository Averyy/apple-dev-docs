# person

**Framework**: Address Book  
**Kind**: property

The contact record being displayed.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var person: ABPerson! { get set }
```

#### Discussion

If the value of this property is `nil`, the view displays a special empty-selection UI.

An exception is raised if the value of this property comes from a shared instance of the address book database. To prevent this, use the [`addressBook`](abaddressbook/addressbook.md) method of [`ABAddressBook`](abaddressbook.md) rather than the [`shared()`](abaddressbook/shared().md) method.

## See Also

- [var editing: Bool](abpersonview/editing.md)
  A Boolean value that indicates whether the person view is in editing mode.
- [var shouldShowLinkedPeople: Bool](abpersonview/shouldshowlinkedpeople.md)
  Indicates whether the person view should display data from person records that are linked with the person record being displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpersonview/person)*