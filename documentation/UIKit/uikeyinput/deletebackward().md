# deleteBackward()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Deletes a character from the displayed text.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
func deleteBackward()
```

```objc
- (void) deleteBackward;
```

## Mentions

- [Handling text interactions in custom keyboards](../handling-text-interactions-in-custom-keyboards.md)

#### Discussion

Remove the character just before the cursor from your class’s backing store and redisplay the text.

## See Also

### Inserting and deleting text
- [func insertText(String)](./inserttext%28_%29.md)
  Inserts a character into the displayed text.
- [var hasText: Bool](./hastext.md)
  A Boolean value that indicates whether the text-entry object has any text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uikeyinput/deletebackward())*