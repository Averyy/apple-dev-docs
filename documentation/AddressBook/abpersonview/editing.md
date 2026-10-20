# editing

**Framework**: Address Book  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the person view is in editing mode.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var editing: Bool { get set }
```

```objc
@property (assign) BOOL editing;
```

#### Discussion

In editing mode, the person view displays additional controls to let the user change the contact’s information.

## See Also

### Working with Person Views
- [var person: ABPerson!](./person.md)
  The contact record being displayed.
- [var shouldShowLinkedPeople: Bool](./shouldshowlinkedpeople.md)
  Indicates whether the person view should display data from person records that are linked with the person record being displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpersonview/editing)*