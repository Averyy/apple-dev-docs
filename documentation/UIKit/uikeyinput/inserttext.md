# insertText(_:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Inserts a character into the displayed text.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func insertText(_ text: String)
```

## Mentions

- [Handling text interactions in custom keyboards](handling-text-interactions-in-custom-keyboards.md)

#### Discussion

Add the character `text` to your class’s backing store at the index corresponding to the cursor and redisplay the text.

## Parameters

- `text`: A string object representing the character typed on the system keyboard.

## See Also

- [func deleteBackward()](uikeyinput/deletebackward.md)
  Deletes a character from the displayed text.
- [var hasText: Bool](uikeyinput/hastext.md)
  A Boolean value that indicates whether the text-entry object has any text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uikeyinput/inserttext(_:))*