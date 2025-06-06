# onCutCommand(perform:)

**Framework**: MusicKit  
**Kind**: method

Adds an action to perform in response to the system’s Cut command.

**Availability**:
- macOS 10.15+

## Declaration

```swift
nonisolated
func onCutCommand(perform payloadAction: (() -> [NSItemProvider])?) -> some View
```

#### Return Value

A view that triggers `action` when a system Cut command occurs.

## Parameters

- `payloadAction`: An action closure that should delete the selected   data and return    items   corresponding to that data, which should be written to the   Clipboard. If   is  , the Cut command is considered   disabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/artworkimage/oncutcommand(perform:))*