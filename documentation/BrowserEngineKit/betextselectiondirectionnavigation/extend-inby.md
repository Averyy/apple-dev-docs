# extend(in:by:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Moves the selection in the specified directions by granularity, in response to different key combinations:

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func extend(in direction: UITextStorageDirection, by granularity: UITextGranularity)
```

#### Discussion

Word = shift + option + left/right paragraph = shift + option + up/down line = shift + command + left/right document = shift + command + up/down

## See Also

- [func extend(in: UITextLayoutDirection)](betextselectiondirectionnavigation/extend(in:).md)
  Extends text selection in the specified directions, such as in response to an arrow key press while shift is held.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextselectiondirectionnavigation/extend(in:by:))*