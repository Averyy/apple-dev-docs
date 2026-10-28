# hasText

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value that indicates whether the text-entry object has any text.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
var hasText: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL hasText;
```

## Mentions

- [Handling text interactions in custom keyboards](../handling-text-interactions-in-custom-keyboards.md)

## Return Value

[`true`](../../Swift/true.md) if the backing store has textual content, [`false`](../../Swift/false.md) otherwise.

## See Also

### Inserting and deleting text
- [func insertText(String)](./inserttext%28_%29.md)
  Inserts a character into the displayed text.
- [func deleteBackward()](./deletebackward%28%29.md)
  Deletes a character from the displayed text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uikeyinput/hastext)*