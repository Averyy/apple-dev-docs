# deleteBackward()

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Deletes a character from the displayed text.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
func deleteBackward()
```

## Mentions

- [Handling text interactions in custom keyboards](handling-text-interactions-in-custom-keyboards.md)

#### Discussion

Remove the character just before the cursor from your class’s backing store and redisplay the text.

## See Also

- [func insertText(String)](uikeyinput/inserttext(_:).md)
  Inserts a character into the displayed text.
- [var hasText: Bool](uikeyinput/hastext.md)
  A Boolean value that indicates whether the text-entry object has any text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uikeyinput/deletebackward())*