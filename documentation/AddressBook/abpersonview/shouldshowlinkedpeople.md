# shouldShowLinkedPeople

**Framework**: Address Book  
**Kind**: property  
**Role**: Instance Property

Indicates whether the person view should display data from person records that are linked with the person record being displayed.

**Availability**:
- macOS 10.8+

## Declaration

```swift
var shouldShowLinkedPeople: Bool { get set }
```

```objc
@property (assign) BOOL shouldShowLinkedPeople;
```

## Discussion

Linked records represent the same actual person, and typically come from different sources.

## See Also

### Working with Person Views
- [var editing: Bool](./editing.md)
  A Boolean value that indicates whether the person view is in editing mode.
- [var person: ABPerson!](./person.md)
  The contact record being displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpersonview/shouldshowlinkedpeople)*