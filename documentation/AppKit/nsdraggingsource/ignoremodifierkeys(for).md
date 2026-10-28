# ignoreModifierKeys(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns whether the modifier keys will be ignored for this dragging session.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func ignoreModifierKeys(for session: NSDraggingSession) -> Bool
```

```objc
- (BOOL) ignoreModifierKeysForDraggingSession:(NSDraggingSession *) session;
```

## Return Value

[`true`](../../Swift/true.md) if the modifier keys will be ignored, [`false`](../../Swift/false.md) otherwise.

## Parameters

- `session`: The dragging session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingsource/ignoremodifierkeys(for:))*