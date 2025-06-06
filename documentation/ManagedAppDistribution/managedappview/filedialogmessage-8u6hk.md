# fileDialogMessage(_:)

**Framework**: ManagedAppDistribution  
**Kind**: method

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with a custom text that is presented to the user, similar to a title.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+

## Declaration

```swift
nonisolated
func fileDialogMessage(_ message: Text?) -> some View
```

## Parameters

- `message`: The optional text to use as the file dialog message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedappview/filedialogmessage(_:)-8u6hk)*