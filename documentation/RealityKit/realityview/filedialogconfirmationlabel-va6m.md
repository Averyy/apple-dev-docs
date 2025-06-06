# fileDialogConfirmationLabel(_:)

**Framework**: RealityKit  
**Kind**: method

On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with a custom confirmation button label.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- visionOS ?+

## Declaration

```swift
nonisolated
func fileDialogConfirmationLabel<S>(_ label: S) -> some View where S : StringProtocol
```

## Parameters

- `label`: The string to use as the label for the confirmation button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityview/filedialogconfirmationlabel(_:)-va6m)*