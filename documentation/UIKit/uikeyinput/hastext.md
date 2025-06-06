# hasText

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

A Boolean value that indicates whether the text-entry object has any text.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
var hasText: Bool { get }
```

## Mentions

- [Handling text interactions in custom keyboards](handling-text-interactions-in-custom-keyboards.md)

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the backing store has textual content, [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

## See Also

- [func insertText(String)](uikeyinput/inserttext(_:).md)
  Inserts a character into the displayed text.
- [func deleteBackward()](uikeyinput/deletebackward.md)
  Deletes a character from the displayed text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uikeyinput/hastext)*