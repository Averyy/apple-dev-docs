# ignoreModifierKeys(for:)

**Framework**: AppKit  
**Kind**: method

Returns whether the modifier keys will be ignored for this dragging session.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func ignoreModifierKeys(for session: NSDraggingSession) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the modifier keys will be ignored, [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

## Parameters

- `session`: The dragging session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingsource/ignoremodifierkeys(for:))*