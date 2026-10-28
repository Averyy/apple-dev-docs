# onCutCommand(perform:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Adds an action to perform in response to the system’s Cut command.

**Availability**:
- macOS 10.15+

## Declaration

```swift
nonisolated
func onCutCommand(perform payloadAction: (() -> [NSItemProvider])?) -> some View
```

## Return Value

A view that triggers `action` when a system Cut command occurs.

## Parameters

- `payloadAction`: An action closure that should delete the selected data and return [`NSItemProvider`](../../Foundation/nsitemprovider.md) items corresponding to that data, which should be written to the Clipboard. If `action` is `nil`, the Cut command is considered disabled.

## See Also

### Copying items using item providers
- [func onCopyCommand(perform: (() -> [NSItemProvider])?) -> some View](./oncopycommand%28perform%29.md)
  Adds an action to perform in response to the system’s Copy command.
- [func onPasteCommand(of:perform:)](./onpastecommand%28of,perform%29.md)
  Adds an action to perform in response to the system’s Paste command.
- [func onPasteCommand(of:validator:perform:)](./onpastecommand%28of,validator,perform%29.md)
  Adds an action to perform in response to the system’s Paste command with items that you validate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/oncutcommand(perform:))*