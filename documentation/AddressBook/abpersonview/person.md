# person

**Framework**: Address Book  
**Kind**: property  
**Role**: Instance Property

The contact record being displayed.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var person: ABPerson! { get set }
```

```objc
@property (retain, readwrite) ABPerson * person;
```

## Discussion

If the value of this property is `nil`, the view displays a special empty-selection UI.

An exception is raised if the value of this property comes from a shared instance of the address book database. To prevent this, use the [`addressBook`](../abaddressbook-swift.class/addressbook.md) method of [`ABAddressBook`](../abaddressbook-swift.class.md) rather than the [`shared()`](../abaddressbook-swift.class/shared%28%29.md) method.

## See Also

### Working with Person Views
- [var editing: Bool](./editing.md)
  A Boolean value that indicates whether the person view is in editing mode.
- [var shouldShowLinkedPeople: Bool](./shouldshowlinkedpeople.md)
  Indicates whether the person view should display data from person records that are linked with the person record being displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpersonview/person)*