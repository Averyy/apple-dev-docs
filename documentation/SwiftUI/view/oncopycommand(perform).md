# onCopyCommand(perform:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Adds an action to perform in response to the system’s Copy command.

**Availability**:
- macOS 10.15+

## Declaration

```swift
nonisolated
func onCopyCommand(perform payloadAction: (() -> [NSItemProvider])?) -> some View
```

#### Return Value

A view that triggers `action` when a system Copy command occurs.

## Parameters

- `payloadAction`: An action closure returning the [`NSItemProvider`](../../Foundation/nsitemprovider.md) items that should be copied to the Clipboard when the Copy command is triggered. If `action` is `nil`, the Copy command is considered disabled.

## See Also

### Copying items using item providers
- [func onCutCommand(perform: (() -> [NSItemProvider])?) -> some View](./oncutcommand%28perform%29.md)
  Adds an action to perform in response to the system’s Cut command.
- [func onPasteCommand(of:perform:)](./onpastecommand%28of,perform%29.md)
  Adds an action to perform in response to the system’s Paste command.
- [func onPasteCommand(of:validator:perform:)](./onpastecommand%28of,validator,perform%29.md)
  Adds an action to perform in response to the system’s Paste command with items that you validate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/oncopycommand(perform:))*