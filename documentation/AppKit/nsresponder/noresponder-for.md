# noResponder(for:)

**Framework**: AppKit  
**Kind**: method

Handles the case where an event or action message falls off the end of the responder chain.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func noResponder(for eventSelector: Selector)
```

#### Discussion

The default implementation beeps if `eventSelector` is [`keyDown(with:)`](nsresponder/keydown(with:).md).

## Parameters

- `eventSelector`: A selector identifying the action or event message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/noresponder(for:))*