# fileDialogMessage(_:)

**Framework**: App Intents  
**Kind**: method

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with a custom message that is presented to the user, similar to a title.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- visionOS ?+

## Declaration

```swift
nonisolated
func fileDialogMessage(_ messageKey: LocalizedStringKey) -> some View
```

## Parameters

- `messageKey`: The key to a localized string to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/filedialogmessage(_:)-10j3f)*