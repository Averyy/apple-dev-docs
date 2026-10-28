# fileDialogMessage(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` with a custom message that is presented to the user, similar to a title.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func fileDialogMessage(_ messageKey: LocalizedStringKey) -> some View
```

**Other overloads**:

```swift
@export(implementation)
nonisolated func fileDialogMessage(_ messageResource: LocalizedStringResource) -> some View
```

```swift
nonisolated
func fileDialogMessage(_ message: Text?) -> some View
```

```swift
nonisolated
func fileDialogMessage<S>(_ message: S) -> some View where S : StringProtocol
```

## Parameters

- `messageKey`: The key to a localized string to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/filedialogmessage(_:)-8rxf4)*