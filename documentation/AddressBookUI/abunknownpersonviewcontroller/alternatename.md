# alternateName

**Framework**: Address Book UI  
**Kind**: property

Provides a value that is displayed instead of the first and last name.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var alternateName: String? { get set }
```

#### Discussion

The alternate name is only for display. It is not saved if this contact is added to the address book database.

## See Also

- [var message: String?](abunknownpersonviewcontroller/message.md)
  Text displayed below [`alternateName`](abunknownpersonviewcontroller/alternatename.md).
- [var displayedPerson: ABRecord](abunknownpersonviewcontroller/displayedperson.md)
  Specifies a person record whose properties are displayed by the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abunknownpersonviewcontroller/alternatename)*