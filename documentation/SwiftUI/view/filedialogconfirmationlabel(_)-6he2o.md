# fileDialogConfirmationLabel(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` with a custom confirmation button label.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func fileDialogConfirmationLabel(_ labelKey: LocalizedStringKey) -> some View
```

**Other overloads**:

```swift
@export(implementation)
nonisolated func fileDialogConfirmationLabel(_ label: LocalizedStringResource) -> some View
```

```swift
nonisolated
func fileDialogConfirmationLabel(_ label: Text?) -> some View
```

```swift
nonisolated
func fileDialogConfirmationLabel<S>(_ label: S) -> some View where S : StringProtocol
```

## Parameters

- `labelKey`: The key to a localized string to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/filedialogconfirmationlabel(_:)-6he2o)*