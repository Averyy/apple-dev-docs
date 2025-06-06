# displayedPerson

**Framework**: Address Book UI  
**Kind**: property

Specifies a person record whose properties are displayed by the view controller.

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

All the properties of `displayedPerson` are displayed by the view controller.

## See Also

- [var alternateName: String?](abunknownpersonviewcontroller/alternatename.md)
  Provides a value that is displayed instead of the first and last name.
- [var message: String?](abunknownpersonviewcontroller/message.md)
  Text displayed below [`alternateName`](abunknownpersonviewcontroller/alternatename.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abunknownpersonviewcontroller/displayedperson)*