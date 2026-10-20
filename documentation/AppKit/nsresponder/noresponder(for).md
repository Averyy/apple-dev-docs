# noResponder(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Handles the case where an event or action message falls off the end of the responder chain.

**Availability**:
- macOS

## Declaration

```swift
func noResponder(for eventSelector: Selector)
```

```objc
- (void) noResponderFor:(SEL) eventSelector;
```

#### Discussion

The default implementation beeps if `eventSelector` is [`keyDown(with:)`](./keydown%28with%29.md).

## Parameters

- `eventSelector`: A selector identifying the action or event message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/noresponder(for:))*