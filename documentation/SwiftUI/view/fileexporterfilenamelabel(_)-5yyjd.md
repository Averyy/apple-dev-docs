# fileExporterFilenameLabel(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

On macOS, configures the `fileExporter` with a text to use as a label for the file name field.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func fileExporterFilenameLabel(_ label: Text?) -> some View
```

**Other overloads**:

```swift
@export(implementation)
nonisolated func fileExporterFilenameLabel(_ label: LocalizedStringResource) -> some View
```

```swift
nonisolated
func fileExporterFilenameLabel(_ labelKey: LocalizedStringKey) -> some View
```

```swift
nonisolated
func fileExporterFilenameLabel<S>(_ label: S) -> some View where S : StringProtocol
```

## Parameters

- `label`: The optional text to use as the label for the file name field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/fileexporterfilenamelabel(_:)-5yyjd)*