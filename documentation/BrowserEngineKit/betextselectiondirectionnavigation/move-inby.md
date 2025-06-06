# move(in:by:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Moves the cursor in the specified directions by granularity, in response to different key combinations:

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func move(in direction: UITextStorageDirection, by granularity: UITextGranularity)
```

#### Discussion

Option + left/right = word Option + up/down = paragraph Command + left/right = line Command + up/down = document


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextselectiondirectionnavigation/move(in:by:))*