# fileDialogMessage(_:)

**Framework**: App Intents  
**Kind**: method

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with a custom message that is presented to the user, similar to a title.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- visionOS ?+

## Declaration

```swift
nonisolated
func fileDialogMessage<S>(_ message: S) -> some View where S : StringProtocol
```

## Parameters

- `message`: The string to use as the file dialog message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutslink/filedialogmessage(_:)-8eir2)*