# onCopyCommand(perform:)

**Framework**: SwiftUI  
**Kind**: method

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

- `payloadAction`: An action closure returning the    items that   should be copied to the Clipboard when the Copy command is   triggered. If   is  , the Copy command is considered   disabled.

## See Also

- [func onCutCommand(perform: (() -> [NSItemProvider])?) -> some View](view/oncutcommand(perform:).md)
  Adds an action to perform in response to the system’s Cut command.
- [func onPasteCommand(of:perform:)](view/onpastecommand(of:perform:).md)
  Adds an action to perform in response to the system’s Paste command.
- [func onPasteCommand(of:validator:perform:)](view/onpastecommand(of:validator:perform:).md)
  Adds an action to perform in response to the system’s Paste command with items that you validate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/oncopycommand(perform:))*