# completes

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates if the combo box tries to complete text entered by the user.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var completes: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the combo box tries to complete what the user types in the text field and every time the user adds characters to the end of the text field, the combo box calls [`completedString(_:)`](nscomboboxcell/completedstring(_:).md); when it is [`false`](https://developer.apple.com/documentation/Swift/false), it does not.

If [`completedString(_:)`](nscomboboxcell/completedstring(_:).md) returns a string that’s longer than the existing string, the combo box replaces the existing string with the returned string and selects the additional characters. If the user is deleting characters or adds characters somewhere besides the end of the string, the combo box does not try to complete it.

## See Also

- [func completedString(String) -> String?](nscomboboxcell/completedstring(_:).md)
  Returns a string from the combo box’s pop-up list that starts with the given substring.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxcell/completes)*