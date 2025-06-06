# fileDialogDefaultDirectory(_:)

**Framework**: App Intents  
**Kind**: method

Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the specified default directory.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func fileDialogDefaultDirectory(_ defaultDirectory: URL?) -> some View
```

## Parameters

- `defaultDirectory`: The directory to show when   the system file dialog launches. If the given file dialog has   a   if stores the user-chosen directory and subsequently   opens with it, ignoring the default value provided in this modifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/filedialogdefaultdirectory(_:))*